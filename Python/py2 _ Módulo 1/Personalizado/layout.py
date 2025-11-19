"""
Módulo layout: exemplos de uso do Rich Layout.
"""

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

def ex_layout(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    layout = Layout()
    layout["right"].split(
        Layout(Panel(text)),
        Layout(Panel("World!"))
    )
    console.print(layout)

def ex_layout_horizontal(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    layout = Layout()
    layout.split_row(
        Layout(Panel(text)),
        Layout(Panel("Outro bloco"))
    )
    console.print(layout)
