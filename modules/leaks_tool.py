from rich.table import Table

def run_leaks(email, console):
    # Base para futuras integraciones de APIs de Leaks
    table = Table(title=f"Búsqueda de Leaks: {email}", header_style="bold red")
    table.add_column("Fuente", style="white")
    table.add_row("Módulo en desarrollo", "Próximamente")
    
    return False, table, "Datos de leaks en desarrollo"
