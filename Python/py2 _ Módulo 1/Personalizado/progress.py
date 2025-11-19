"""
Módulo progresso: exemplos de uso do Rich Progress.
"""

import time
from rich.progress import Progress

def barra(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    with Progress() as progress:
        tarefa = progress.add_task(text, total=10)
        while not progress.finished:
            progress.update(tarefa, advance=1)
            time.sleep(0.2)

def barras_multiplas(text: str, isArquivo: bool):
    if isArquivo:
        with open(text, "r") as f:
            text = f.read()

    with Progress() as progress:
        t1 = progress.add_task("[red]Downloading...", total=5)
        t2 = progress.add_task("[green]Processing...", total=5)
        while not progress.finished:
            progress.update(t1, advance=1)
            progress.update(t2, advance=1)
            time.sleep(0.3)
