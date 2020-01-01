# -*- coding: utf-8 -*-
"""Console script for najia."""
import sys

import click
from najia.najia import Najia

@click.command()
@click.option('-p', '--params', default='221242', help='摇卦参数')
@click.option('-g', '--gender', default='男', help='摇卦人性别.')
@click.option('-l', '--lunar', default=False, help='是否阴历.')
@click.option('-d', '--date', default='solar', help='日期 YYYY-MM-DD hh:mm.')
def main(params, gender, lunar, date):
    """Console script for najia."""
    # click.echo(locals())
    # click.echo("Replace this message by putting your code into najia.cli.main")
    # click.echo("See click documentation at https://click.palletsprojects.com/")
    params = params.replace(',', '')
    params = [int(x) for x in params]
    
    gua = Najia().compile(params=params, gender=2, date=date)
    res = gua.render()
    
    print(res)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
