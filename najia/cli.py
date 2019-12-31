# -*- coding: utf-8 -*-

"""Console script for najia."""
import sys

import click


@click.command()
def main(args=None):
    """Console script for najia."""
    click.echo("Replace this message by putting your code into "
               "najia.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
