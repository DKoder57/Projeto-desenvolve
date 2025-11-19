"""
Módulo painel: exemplos de uso do Rich Panel.
"""

from rich.console import Console
from rich.panel import Panel

console = Console()

def painel_simples(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()
    console.print(Panel(text, title="Painel"))

def painel_colorido(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()
    console.print(Panel(text, title="Welcome", subtitle="Thank you"))
