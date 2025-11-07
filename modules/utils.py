import os
import platform

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()


def clear_screen() -> None:
    """Limpa o terminal de acordo com o sistema operacional."""
    system = platform.system().lower()
    command = "cls" if system == "windows" else "clear"
    os.system(command)


def print_banner() -> None:
    """Exibe um banner colorido com o nome da IA."""
    title = Text("IA de Minecraft", style="bold green")
    subtitle = Text("Seu guia amigável para aventuras no bloco!", style="italic cyan")
    panel = Panel.fit(
        Text.assemble(title, "\n", subtitle),
        border_style="bright_green",
        title="Bem-vindo",
        title_align="left",
    )
    console.print(panel)

