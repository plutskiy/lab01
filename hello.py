from typing import Optional

import typer


def main(
    name: str,
    lastname: Optional[str] = typer.Option(None, "--lastname", "-l", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
) -> None:
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    # формальное приветствие используется, если явно передан флаг --formal/-f
    greeting = "Добрый день" if formal else "Привет"
    full_name = f"{name} {lastname}".strip() if lastname else name

    typer.echo(f"{greeting}, {full_name}!")


if __name__ == "__main__":
    typer.run(main)
