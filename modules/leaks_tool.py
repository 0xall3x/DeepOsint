import os
import requests
from rich.table import Table
from rich.progress import Progress

HIBP_BREACH_URL = "https://haveibeenpwned.com/api/v3/breachedaccount/{}"
USER_AGENT = "DeepOsint-LeaksModule"


def run_leaks(email, console):
    report_content = f"REPORTE DE FILTRACIONES (HaveIBeenPwned): {email}\n" + "=" * 40 + "\n"

    table = Table(title=f"Búsqueda de Leaks: {email}", header_style="bold red")
    table.add_column("Brecha", style="white")
    table.add_column("Fecha", style="yellow")
    table.add_column("Dominio", style="cyan")

    api_key = os.environ.get("HIBP_API_KEY")
    if not api_key:
        report_content += (
            "No se configuró HIBP_API_KEY. Consigue una API key en "
            "https://haveibeenpwned.com/API/Key y expórtala como variable de entorno "
            "(export HIBP_API_KEY=tu_key).\n"
        )
        console.print("[yellow][!] HIBP_API_KEY no configurada. Módulo de leaks omitido.[/yellow]")
        return False, table, report_content

    headers = {"hibp-api-key": api_key, "User-Agent": USER_AGENT}

    with Progress(transient=True) as progress:
        progress.add_task(f"[bold red]HaveIBeenPwned: Buscando filtraciones de {email}...", total=None)
        try:
            response = requests.get(
                HIBP_BREACH_URL.format(email),
                headers=headers,
                params={"truncateResponse": "false"},
                timeout=15,
            )
        except requests.RequestException as e:
            report_content += f"Error conectando con HaveIBeenPwned: {e}\n"
            return False, table, report_content

    if response.status_code == 404:
        report_content += "No se encontraron filtraciones para este email.\n"
        return False, table, report_content

    if response.status_code == 401:
        report_content += "API Key de HaveIBeenPwned inválida.\n"
        return False, table, report_content

    if response.status_code == 429:
        report_content += "Límite de peticiones a HaveIBeenPwned alcanzado. Inténtalo más tarde.\n"
        return False, table, report_content

    if response.status_code != 200:
        report_content += f"HaveIBeenPwned devolvió un error inesperado: {response.status_code}\n"
        return False, table, report_content

    found = False
    for breach in response.json():
        name = breach.get("Title") or breach.get("Name", "Desconocido")
        date = breach.get("BreachDate", "N/A")
        domain = breach.get("Domain") or "N/A"
        table.add_row(name, date, domain)
        report_content += f"[Breach] {name} | Fecha: {date} | Dominio: {domain}\n"
        found = True

    return found, table, report_content
