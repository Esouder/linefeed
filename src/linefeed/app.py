from html import parser
from logging import config
from .api import api
from .config_manager import ConfigManager
from .formatter import Formatter
from .print_handler import PrintHandler
from fastapi import FastAPI
import argparse
from uvicorn import Config, Server


def create_app() -> None:
    """
    Initializes and configures the FastAPI application with the necessary components.
    This includes loading configurations, setting up the formatter and print handler,
    and attaching them to the app's state for dependency injection.

    The application is configured to handle print commands and manage print jobs
    through defined API endpoints.

    Returns
    -------
    None
        The function modifies the FastAPI app in place and does not return a value.
    """
    parser = argparse.ArgumentParser(
        description="Linefeed: A networked text printing service."
    )

    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to the configuration file (default: config.yaml)",
    )
    args = parser.parse_args()

    config_manager = ConfigManager(args.config)

    formatter = Formatter(config_manager.format_config)
    print_handler = PrintHandler(config_manager.device_config)
    print_handler.start()

    api.state.formatter = formatter
    api.state.print_handler = print_handler

    server_config = Config(
        app=api,
        host=config_manager.api_config.port,
        port=config_manager.api_config.port,
        workers=1,
    )
    server = Server(server_config)
    server.run()


if __name__ == "__main__":
    create_app()
