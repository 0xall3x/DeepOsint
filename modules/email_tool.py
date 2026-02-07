import subprocess
from rich.table import Table
from rich.progress import Progress

def run_email(email, console):
    report_content = "SERVICIO | ESTADO\n" + "="*30 + "\n"
    with Progress(transient=True) as progress:
        progress.add_task(f"[bold cyan]Rastreando email: {email}...", total=None)
        result = subprocess.run(["holehe", email, "--only-used"], capture_output=True, text=True)
    
    table = Table(title=f"Inteligencia de Email: {email}", header_style="bold cyan")
    table.add_column("Servicio", style="white"); table.add_column("Estado", style="bold green")
    
    found = False
    for line in result.stdout.split('\n'):
        if "[+]" in line:
            clean_name = line.replace("[+]", "").strip().split(' ')[0]
            table.add_row(clean_name, "Registrado")
            report_content += f"{clean_name}: REGISTRADO\n"
            found = True
            
    return found, table, report_content
