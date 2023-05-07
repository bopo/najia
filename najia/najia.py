import json
import logging
import os
from pathlib import Path

import arrow
from jinja2 import Template

from .const import GANS
from .const import GUA5
from .const import GUA64
from .const import GUAS
from .const import SYMBOL
from .const import XING5
from .const import YAOS
from .const import ZHI5
from .const import ZHIS
from .utils import get_god6
from .utils import get_guaci
from .utils import get_najia
from .utils import get_qin6
from .utils import get_type
from .utils import GZ5X
from .utils import palace
from .utils import set_shi_yao

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


class Najia(object):

    def __init__(self, verbose=None):
        self.verbose = (verbose, 2)[verbose > 2] or 0
        self.bian = None  # 变卦
        self.hide = None  # 伏神
        self.data = None

    @staticmethod
    def _gz(cal):
        """
        获取干支
        :param cal:
        :return:
        """
        return GANS[cal.tg] + ZHIS[cal.dz]

    @staticmethod
    def _cn(cal):
        """
        转换中文干支
        :param cal:
        :return:
        """
        return GANS[cal.tg] + ZHIS[cal.dz]

    @staticmethod
    def _daily(date=None):
        """
        计算日期
        :param date:
        :return:
        """
        # lunar = sxtwl.Lunar()
        # daily = lunar.getDayBySolar(date.year, date.month, date.day)
        # hour = lunar.getShiGz(daily.Lday2.tg, date.hour)

        from lunar_python import Solar

        solar = Solar.fromYmdHms(date.year, date.month, date.day, date.hour, 0, 0)
        lunar = solar.getLunar()

        ganzi = lunar.getBaZi()

        result = {
            # 'xkong': xkong(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]])),
            'xkong': lunar.getDayXunKong(),
            # 'month': daily.Lmonth2,
            # 'year' : daily.Lyear2,
            # 'day'  : daily.Lday2,
            # 'hour' : hour,
            # 'cn'   : {
            #     'month': self._gz(daily.Lmonth2),
            #     'year' : self._gz(daily.Lyear2),
            #     'day'  : self._gz(daily.Lday2),
            #     'hour' : self._gz(hour),
            # },
            'gz': {
                'month': ganzi[1],
                'year': ganzi[0],
                'day': ganzi[2],
                'hour': ganzi[3],
            }
        }
        # pprint(result)
        return result

    @staticmethod
    def _hidden(gong=None, qins=None):
        """
        计算伏神卦

        :param gong:
        :param qins:
        :return:
        """
        if gong is None:
            raise Exception('')

        if qins is None:
            raise Exception('')

        if len(set(qins)) < 5:
            mark = YAOS[gong] * 2

            logger.debug(mark)

            # 六亲
            qin6 = [(get_qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in get_najia(mark)]

            # 干支五行
            qinx = [GZ5X(x) for x in get_najia(mark)]
            seat = [qin6.index(x) for x in list(set(qin6).difference(set(qins)))]

            return {
                'name': GUA64.get(mark),
                'mark': mark,
                'qin6': qin6,
                'qinx': qinx,
                'seat': seat,
            }

        return None

    @staticmethod
    def _transform(params=None, gong=None):
        """
        计算变卦

        :param params:
        :return:
        """

        if params is None:
            raise Exception('')

        if type(params) == str:
            params = [x for x in params]

        if len(params) < 6:
            raise Exception('')

        if 3 in params or 4 in params:
            mark = ''.join(['1' if v in [1, 4] else '0' for v in params])
            qin6 = [(get_qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in get_najia(mark)]
            qinx = [GZ5X(x) for x in get_najia(mark)]

            return {
                'name': GUA64.get(mark),
                'mark': mark,
                'qin6': qin6,
                'qinx': qinx,
                'gong': GUAS[palace(mark, set_shi_yao(mark)[0])],
            }

        return None

    def compile(self, params=None, gender=None, date=None, title=None, guaci=False, **kwargs):
        """
        根据参数编译卦

        :param guaci:
        :param title:
        :param gender:
        :param params:
        :param date:
        :return:
        """

        title = (title, '')[not title]
        solar = arrow.now() if date is None else arrow.get(date)
        lunar = self._daily(solar)

        # gender = '男' if gender == 1 else '女'
        gender = ('', gender)[bool(gender)]

        # 卦码
        mark = ''.join([str(int(p) % 2) for p in params])

        shiy = set_shi_yao(mark)  # 世应爻

        # 卦宫
        gong = palace(mark, shiy[0])  # 卦宫

        # 卦名
        name = GUA64[mark]

        # 六亲
        qin6 = [(get_qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in get_najia(mark)]
        qinx = [GZ5X(x) for x in get_najia(mark)]

        # logger.debug(qin6)

        # 六神
        # god6 = God6(''.join([GANS[lunar['day'].tg], ZHIS[lunar['day'].dz]]))
        god6 = get_god6(lunar['gz']['day'])

        # 动爻位置
        dong = [i for i, x in enumerate(params) if x > 2]
        # logger.debug(dong)

        # 伏神
        hide = self._hidden(gong, qin6)

        # 变卦
        bian = self._transform(params=params, gong=gong)

        self.data = {
            'params': params,
            'gender': gender,
            'title': title,
            'guaci': guaci,
            'solar': solar,
            'lunar': lunar,
            'god6': god6,
            'dong': dong,
            'name': name,
            'mark': mark,
            'gong': GUAS[gong],
            'shiy': shiy,
            'qin6': qin6,
            'qinx': qinx,
            'bian': bian,
            'hide': hide,
        }

        # logger.debug(self.data)

        return self

    def gua_type(self, i):
        return

    def render(self):
        """

        :return:
        """
        tpl = Path(__file__).parent / 'data' / 'standard.tpl'
        tpl = tpl.read_text(encoding='utf-8')

        empty = '\u3000' * 6
        rows = self.data

        # symbal = ['━　━', '━━━━', '━　━', '○→', '×→']
        # yaos = ['▅▅  ▅▅', '▅▅▅▅▅▅', '▅▅  ▅▅', '○→', '×→']
        symbal = SYMBOL[self.verbose]

        rows['dyao'] = [symbal[x] if x in (3, 4) else '' for x in self.data['params']]

        rows['main'] = {}
        rows['main']['mark'] = [symbal[int(x)] for x in self.data['mark']]
        rows['main']['type'] = get_type(self.data['mark'])

        rows['main']['gong'] = rows['gong']
        rows['main']['name'] = rows['name']
        rows['main']['indent'] = '\u3000' * 2

        if rows.get('hide'):
            rows['hide']['qin6'] = [' %s%s ' % (rows['hide']['qin6'][x], rows['hide']['qinx'][x]) if x in rows['hide']['seat'] else empty for x in range(0, 6)]
            rows['main']['indent'] += empty
        else:
            rows['main']['indent'] += '\u3000' * 1
            rows['hide'] = {'qin6': ['  ' for _ in range(0, 6)]}

        rows['main']['display'] = '{indent}{name} ({gong}-{type})'.format(**rows['main'])

        if rows.get('bian'):
            hide = (8, 19)[bool(rows.get('hide'))]
            rows['bian']['type'] = get_type(rows['bian']['mark'])
            rows['bian']['indent'] = (hide - len(rows['main']['display'])) * '\u3000'

            if rows['bian']['qin6']:
                # 变卦六亲问题
                rows['bian']['qin6'] = [f'{rows["bian"]["qin6"][x]}{rows["bian"]["qinx"][x]}' if x in self.data['dong'] else f'  {rows["bian"]["qin6"][x]}{rows["bian"]["qinx"][x]}'
                                        for x in range(0, 6)]

            if rows['bian']['mark']:
                rows['bian']['mark'] = [x for x in rows['bian']['mark']]
                rows['bian']['mark'] = [symbal[int(rows['bian']['mark'][x])] for x in range(0, 6)]
        else:
            rows['bian'] = {'qin6': [' ' for _ in range(0, 6)], 'mark': [' ' for _ in range(0, 6)]}

        shiy = []

        # 显示世应字
        for x in range(0, 6):
            if x == self.data['shiy'][0] - 1:
                shiy.append('世')
            elif x == self.data['shiy'][1] - 1:
                shiy.append('应')
            else:
                shiy.append('  ')

        rows['shiy'] = shiy

        if self.data['guaci']:
            rows['guaci'] = get_guaci(rows['name'])
            # rows['guaci'] = json.load(open(os.path.join(os.path.dirname(__file__), 'data/dd.json'))).get(rows['name'])
            # rows['guaci'] = rows.get('guaci', '').replace('********************', '').replace('　象曰：', '象曰：')

        template = Template(tpl)
        return template.render(**rows)

    def export(self):
        solar, params = self.data
        return solar, params

    def predict(self):
        return
