from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

def print_banner():
    # ASCII Art más estilizado (Font: Slant o Shadow)
    ascii_art = r"""
    ____                        ____  _____ ___ _   _ _____ 
   |  _ \  ___  ___ _ __       / __ \/ ___/|_ _| \ | |_   _|
   | | | |/ _ \/ _ \ '_ \     | |  | \___ \ | ||  \| | | |  
   | |_| |  __/  __/ |_) |    | |__| |___) || || |\  | | |  
   |____/ \___|\___| .__/      \____/____/|___|_| \_| |_|  
                   |_|                                      
    """
    
    # Creamos el texto con un degradado de azul a cian
    banner_text = Text(ascii_art, style="bold dodger_blue1")
    
    # Añadimos la firma de los autores con un estilo diferente
    signature = Text("\nBy 0xall3x & veyron92i", style="italic white")
    
    # Combinamos todo en un Panel centrado
    full_banner = Text.assemble(banner_text, signature)
    
    panel = Panel(
        Align.center(full_banner),
        border_style="bright_blue",
        subtitle="[bold white]v1.0.0[/bold white]",
        subtitle_align="right"
    )
    
    console.print(panel)

if __name__ == "__main__":
    print_banner()
