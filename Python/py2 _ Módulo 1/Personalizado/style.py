"""
Módulo estilo: exemplos de uso do Rich Style.
"""

from rich.console import Console
from rich.style import Style

console = Console()

def estilo_ciano(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    base_style = Style.parse("cyan")
    console.print(text, style=base_style)

def estilo_sublinhado(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    base_style = Style.parse("cyan")
    console.print(text, style=base_style + Style(underline=True))
