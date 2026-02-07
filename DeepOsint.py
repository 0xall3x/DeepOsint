import argparse
import os
from datetime import datetime
from rich.console import Console

# Importamos tus módulos y el banner
from utils.banner import print_banner
from modules.username_tool import run_username
from modules.email_tool import run_email
from modules.leaks_tool import run_leaks

console = Console()

def save_report(target, data_type, content):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_target = str(target).replace("@", "_at_").replace(".", "_")
    filename = f"reports/{data_type}_{safe_target}_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    console.print(f"\n[bold green][+] Reporte guardado en:[/bold green] [white]{filename}[/white]")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="DeepOsint - Massive Intelligence Tool")
    parser.add_argument("--username", help="Investigación de Redes + Instagram")
    parser.add_argument("--email", help="Investigación de Cuentas + Leaks")
    parser.add_argument("--session", help="Cookie sessionid de Instagram (opcional)", default=None)
    args = parser.parse_args()

    if args.username:
        console.print(f"[bold yellow][!] Iniciando Inteligencia de Usuario para: {args.username}[/bold yellow]\n")
        # Pasamos la sesión aquí
        found, content = run_username(args.username, console, session_id=args.session)
        if found:
            save_report(args.username, "USER_INTEL", content)
        else:
            console.print("[red][!] No se encontró información relevante.")

    elif args.email:
        console.print(f"[bold yellow][!] Iniciando Inteligencia de Email para: {args.email}[/bold yellow]\n")
        found_e, table_e, content_e = run_email(args.email, console)
        if found_e:
            console.print(table_e)
            save_report(args.email, "EMAIL_ACCOUNTS", content_e)
        
        found_l, table_l, content_l = run_leaks(args.email, console)
        if found_l:
            console.print(table_l)
            save_report(args.email, "EMAIL_LEAKS", content_l)
    else:
        console.print("[yellow]Uso: python DeepOsint.py --username <user> [--session <id>] | --email <email>[/yellow]")

if __name__ == "__main__":
    main()
