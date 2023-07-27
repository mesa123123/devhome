"""
Module String
"""
import os
from typing import Optional
from typing_extensions import Annotated
from rich.console import Console

import typer

console = Console()


def main(name: Annotated[Optional[str], typer.Argument()] = None):
    if name is None:
        dev_route = f"/home/{os.environ['USER']}/dev"
        console.print(os.listdir(dev_route), style="blue")
    else:
        console.print("No dev folder found")


if __name__ == "__main__":
    typer.run(main)
