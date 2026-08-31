import subprocess
from rich.table import Table
from rich.progress import Progress

SECTION_HEADERS = {
    "hosts found": "Host",
    "emails found": "Email",
    "ips found": "IP",
}


def _parse_theharvester(output):
    """Extrae hosts/emails/IPs de la salida de consola de theHarvester."""
    results = []
    current_type = None

    for raw_line in output.split("\n"):
        line = raw_line.strip()
        lower = line.lower()

        matched_header = None
        for header, label in SECTION_HEADERS.items():
            if lower.startswith(f"[*] {header}"):
                matched_header = label
                break

        if matched_header:
            current_type = matched_header
            continue

        if not line or line.startswith("[*]") or line.startswith("---"):
            current_type = None
            continue

        if current_type:
            results.append((current_type, line))

    return results


def run_domain(domain, console):
    report_content = f"REPORTE DE DOMINIO: {domain}\n" + "=" * 40 + "\n"
    found = False

    table = Table(title=f"theHarvester: {domain}", header_style="bold green")
    table.add_column("Tipo", style="cyan")
    table.add_column("Dato", style="white")

    with Progress(transient=True) as progress:
        progress.add_task(f"[bold green]theHarvester: Recolectando datos de {domain}...", total=None)
        try:
            # crtsh y duckduckgo no requieren API key
            result = subprocess.run(
                ["theHarvester", "-d", domain, "-b", "crtsh,duckduckgo"],
                capture_output=True, text=True
            )
            entries = _parse_theharvester(result.stdout)
            seen = set()
            for kind, value in entries:
                key = (kind, value)
                if key in seen:
                    continue
                seen.add(key)
                table.add_row(kind, value)
                report_content += f"[{kind}] {value}\n"
                found = True
        except FileNotFoundError:
            report_content += "theHarvester no está instalado.\n"

    return found, table, report_content
