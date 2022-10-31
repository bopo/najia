import random
import sys

import click

from . import __version__
from .najia import Najia


@click.command()
@click.help_option('-h', '--help')
@click.version_option(__version__, "-V", "--version", prog_name="Najia", message="%(prog)s: version %(version)s", )
@click.option('-p', '--params', default=None, help='摇卦参数')
@click.option('-g', '--gender', default=1, help='摇卦人性别.')
@click.option('-l', '--lunar', default=False, help='是否阴历.')
@click.option('-t', '--title', default='', help='求卦问卜事情.')
@click.option('-c', '--guaci', is_flag=True, help='是否显示卦辞.')
@click.option('-d', '--date', default=None, help='日期 YYYY-MM-DD hh:mm.')
def main(params, gender, lunar, date, title, guaci):
    params = [random.randint(1, 4) for _ in range(0, 6)] if params is None else params
    params = [int(x) for x in params.replace(',', '')] if type(params) == str else params

    gua = Najia().compile(params=params, gender=gender, date=date, title=title, guaci=guaci)
    res = gua.render()

    print(res)

    return 0


if __name__ == '__main__':
    sys.exit(main())  # pragma: no cover
