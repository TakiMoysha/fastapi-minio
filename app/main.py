import os

from app.asgi import create_asgi


def run_cli():
    from fastapi_cli.cli import main as cli_main

    os.environ.setdefault("FASTAPI_APP", "app.asgi:app")

    cli_main()


if __name__ == "__main__":
    application = create_asgi()
