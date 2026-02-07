import subprocess
import os
from rich.table import Table
from rich.progress import Progress

def run_username(username, console, session_id=None):
    report_content = f"REPORTE INTEGRAL: {username}\n" + "="*40 + "\n"
    found_any = False
    touatis_output = ""
    results_sherlock = []
    
    toutatis_path = "./venv/bin/toutatis"

    with Progress(transient=True) as progress:
        # --- TAREA 1: SHERLOCK (Lectura directa de consola) ---
        task = progress.add_task(f"[bold magenta]Sherlock: Buscando {username}...", total=None)
        
        # Ejecutamos sherlock y leemos línea a línea
        proc = subprocess.Popen(
            ["sherlock", username, "--timeout", "5"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in proc.stdout:
            if "[+]" in line:
                # Ejemplo: "[+] Instagram: https://instagram.com/user"
                clean_line = line.replace("[+]", "").strip()
                if ":" in clean_line:
                    site, url = clean_line.split(": ", 1)
                    results_sherlock.append((site, url))
        proc.wait()

        # --- TAREA 2: TOUATIS ---
        if session_id:
            progress.add_task("[bold cyan]Touatis: Analizando Instagram...", total=None)
            res = subprocess.run([toutatis_path, "-u", username, "-s", session_id], 
                                 capture_output=True, text=True)
            touatis_output = res.stdout

    # --- MOSTRAR RESULTADOS SHERLOCK ---
    if results_sherlock:
        table_s = Table(title=f"Hallazgos Sherlock: {username}", header_style="bold magenta")
        table_s.add_column("Plataforma", style="cyan")
        table_s.add_column("Enlace", style="green")
        
        for site, url in results_sherlock:
            table_s.add_row(site, url)
            report_content += f"[Sherlock] {site}: {url}\n"
        
        console.print(table_s)
        found_any = True

    # --- PROCESAR TOUATIS ---
    if touatis_output:
        if "Rate limit" in touatis_output:
            console.print("[bold red][!] Instagram detectó actividad inusual (Rate Limit).[/bold red]")
            report_content += "\n[Instagram] Error: Rate Limit detectado.\n"
        elif "Username" in touatis_output:
            table_t = Table(title=f"Instagram Intel: {username}", header_style="bold cyan")
            table_t.add_column("Campo", style="white")
            table_t.add_column("Dato", style="yellow")
            
            report_content += "\n[Instagram Data]\n"
            for line in touatis_output.split('\n'):
                if ":" in line and "[*]" not in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        k, v = parts[0].strip(), parts[1].strip()
                        table_t.add_row(k, v)
                        report_content += f"{k}: {v}\n"
                        found_any = True
            console.print(table_t)

    return found_any, report_content
