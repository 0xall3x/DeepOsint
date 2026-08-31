import subprocess
from rich.table import Table
from rich.progress import Progress

def run_email(email, console):
    report_content = "SERVICIO | ESTADO\n" + "="*30 + "\n"
    seen_services = set()

    table = Table(title=f"Inteligencia de Email: {email}", header_style="bold cyan")
    table.add_column("Servicio", style="white"); table.add_column("Estado", style="bold green")

    found = False

    with Progress(transient=True) as progress:
        # --- HOLEHE ---
        progress.add_task(f"[bold cyan]Holehe: Rastreando email {email}...", total=None)
        result = subprocess.run(["holehe", email, "--only-used"], capture_output=True, text=True)

        for line in result.stdout.split('\n'):
            if "[+]" in line:
                clean_name = line.replace("[+]", "").strip().split(' ')[0]
                if clean_name.lower() not in seen_services:
                    table.add_row(clean_name, "Registrado")
                    report_content += f"[Holehe] {clean_name}: REGISTRADO\n"
                    seen_services.add(clean_name.lower())
                    found = True

        # --- SOCIALSCAN (cobertura adicional de plataformas) ---
        progress.add_task(f"[bold blue]Socialscan: Ampliando búsqueda de {email}...", total=None)
        try:
            res_s = subprocess.run(["socialscan", email], capture_output=True, text=True)
            for line in res_s.stdout.split('\n'):
                # Ejemplo: "user@mail.com  Instagram        Taken"
                if "Taken" in line:
                    parts = line.split()
                    if len(parts) >= 2:
                        service = parts[1]
                        if service.lower() not in seen_services:
                            table.add_row(service, "Registrado")
                            report_content += f"[Socialscan] {service}: REGISTRADO\n"
                            seen_services.add(service.lower())
                            found = True
        except FileNotFoundError:
            pass

    return found, table, report_content
