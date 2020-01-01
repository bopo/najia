# -*- coding: utf-8 -*-
"""Console script for najia."""
import sys,random
from time import sleep

import click
from najia.najia import Najia

@click.command()
@click.option('-p', '--params', default=None, help='摇卦参数')
@click.option('-g', '--gender', default=1, help='摇卦人性别.')
@click.option('-l', '--lunar', default=False, help='是否阴历.')
@click.option('-d', '--date', default='solar', help='日期 YYYY-MM-DD hh:mm.')
def main(params, gender, lunar, date):
    """Console script for najia."""
    # click.echo(locals())
    # click.echo("Replace this message by putting your code into najia.cli.main")
    # click.echo("See click documentation at https://click.palletsprojects.com/")

    params = [random.randint(1, 4) for x in range(0, 6)] if params is None else params
    params = [int(x) for x in params.replace(',', '')] if type(params) == str else params
    
    gua = Najia().compile(params=params, gender=gender, date=date)
    res = gua.render()
    
    print(res)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
