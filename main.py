from __future__ import annotations

import sys
from typing import NoReturn

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.prompt import Prompt
from rich.status import Status

from modules import chat, tips
from modules.utils import clear_screen, print_banner


console = Console()


def startup() -> OpenAI:
    """Carrega variáveis de ambiente e inicializa o cliente OpenAI."""
    load_dotenv()
    client = OpenAI()
    chat.set_client(client)
    return client


def main() -> None:
    """Executa o loop principal da aplicação."""
    startup()
    clear_screen()
    print_banner()
    console.print("[bold cyan]Digite 'sair' ou 'exit' para encerrar a conversa.[/]\n")

    while True:
        user_input = Prompt.ask("[bold yellow]Você")
        normalized = user_input.strip().lower()

        if normalized in {"sair", "exit"}:
            console.print("\n[bold green]Até a próxima! Bons blocos![/]")
            break

        if not normalized:
            console.print("[red]Ops! Digite algo para que eu possa ajudar.[/]")
            continue

        with console.status("Carregando os blocos...", spinner="dots") as status:  # type: Status
            try:
                response = chat.generate_response(user_input)
                status.stop()
            except Exception as exc:  # pragma: no cover - graceful runtime handling
                status.stop()
                console.print(f"[red]Erro ao gerar resposta: {exc}[/]")
                continue

        console.print(f"[bold green]IA:[/] {response}\n")

        if Prompt.ask(
            "[italic cyan]Quer uma dica aleatória de Minecraft agora?[/]",
            choices=["s", "n"],
            default="n",
            show_choices=False,
        ).lower() == "s":
            console.print(f"[magenta]- {tips.get_random_tip()}[/]\n")


def _handle_keyboard_interrupt() -> NoReturn:
    console.print("\n[bold green]Até a próxima! Bons blocos![/]")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        _handle_keyboard_interrupt()

