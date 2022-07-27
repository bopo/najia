# -*- coding: utf-8 -*-
import arrow
import json
import logging
import os
import sxtwl
from jinja2 import Template

from najia.const import GANS, GUA5, GUA64, XING5, YAOS, ZHI5, ZHIS
from najia.utils import GZ5X, God6, Qin6, getNajia, palace, setShiYao, xkong

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


class Najia(object):
    bian = None  # 变卦
    hide = None  # 伏神
    data = None

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

        :param cal:
        :return:
        """
        return GANS[cal.tg] + ZHIS[cal.dz]

    def _daily(self, date=None):
        lunar = sxtwl.Lunar()
        daily = lunar.getDayBySolar(date.year, date.month, date.day)
        hour = lunar.getShiGz(daily.Lday2.tg, date.hour)

        return {
            'xkong': xkong(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]])),
            'month': daily.Lmonth2,
            'year': daily.Lyear2,
            'day': daily.Lday2,
            'hour': hour,
            'gz': {
                'month': self._gz(daily.Lmonth2),
                'year': self._gz(daily.Lyear2),
                'day': self._gz(daily.Lday2),
                'hour': self._gz(hour),
            },
            'cn': {
                'month': self._gz(daily.Lmonth2),
                'year': self._gz(daily.Lyear2),
                'day': self._gz(daily.Lday2),
                'hour': self._gz(hour),
            }
        }

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
            qin6 = [(Qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(mark)]

            # 干支五行
            qinx = [GZ5X(x) for x in getNajia(mark)]
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
    def _transform(params=None):
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
            gong = palace(mark, setShiYao(mark)[0])  # 卦宫
            qin6 = [(Qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(mark)]
            qinx = [GZ5X(x) for x in getNajia(mark)]

            return {
                'name': GUA64.get(mark),
                'mark': mark,
                'qin6': qin6,
                'qinx': qinx,
            }

        return None

    def compile(self, params=None, gender=1, date=None, title=None, guaci=False):
        """
        根据参数编译卦

        :param guaci:
        :param title:
        :param gender:
        :param params:
        :param date:
        :return:
        """
        solar = arrow.now() if date is None else arrow.get(date)
        lunar = self._daily(solar)

        gender = '男' if gender == 1 else '女'

        # 卦码
        mark = ''.join([str(int(l) % 2) for l in params])

        logger.debug(mark)

        shiy = setShiYao(mark)  # 世应爻

        # 卦宫
        gong = palace(mark, shiy[0])  # 卦宫

        # 卦名
        name = GUA64[mark]

        # 六亲
        qin6 = [(Qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(mark)]
        qinx = [GZ5X(x) for x in getNajia(mark)]

        logger.debug(qin6)

        # 六神
        god6 = God6(''.join([GANS[lunar['day'].tg], ZHIS[lunar['day'].dz]]))

        # 动爻位置
        dong = [i for i, x in enumerate(params) if x > 2]
        logger.debug(dong)

        # 伏神
        hide = self._hidden(gong, qin6)

        # 变卦
        bian = self._transform(params=params)

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
            'gong': gong,
            'shiy': shiy,
            'qin6': qin6,
            'qinx': qinx,
            'bian': bian,
            'hide': hide,
        }

        logger.debug(self.data)

        return self

    def render(self):
        """

        :return:
        """
        tpl = '''{{gender}}测：{{title}}

公历：{{solar.year}}年 {{solar.month}}月 {{solar.day}}日 {{solar.hour}}时 {{solar.minute}}分
干支：{{lunar.gz.year}}年 {{lunar.gz.month}}月 {{lunar.gz.day}}日 {{lunar.gz.hour}}时 （旬空：{{lunar.xkong}})

得「{{name}}」{% if bian.name %}之「{{bian.name}}」{% endif %}卦

{{god6.5}}{{hide.qin6.5}}{{qin6.5}}{{qinx.5}} {{mark.5}} {{shiy.5}} {{dyao.5}} {{bian.qin6.5}} {{bian.mark.5}}
{{god6.4}}{{hide.qin6.4}}{{qin6.4}}{{qinx.4}} {{mark.4}} {{shiy.4}} {{dyao.4}} {{bian.qin6.4}} {{bian.mark.4}}
{{god6.3}}{{hide.qin6.3}}{{qin6.3}}{{qinx.3}} {{mark.3}} {{shiy.3}} {{dyao.3}} {{bian.qin6.3}} {{bian.mark.3}}
{{god6.2}}{{hide.qin6.2}}{{qin6.2}}{{qinx.2}} {{mark.2}} {{shiy.2}} {{dyao.2}} {{bian.qin6.2}} {{bian.mark.2}}
{{god6.1}}{{hide.qin6.1}}{{qin6.1}}{{qinx.1}} {{mark.1}} {{shiy.1}} {{dyao.1}} {{bian.qin6.1}} {{bian.mark.1}}
{{god6.0}}{{hide.qin6.0}}{{qin6.0}}{{qinx.0}} {{mark.0}} {{shiy.0}} {{dyao.0}} {{bian.qin6.0}} {{bian.mark.0}}

{% if guaci %}{{ guaci }}{% endif %}'''

        rows = self.data
        yaos = ['``', '` ', '``', '○→', '×→']

        rows['dyao'] = [yaos[x] if x in (3, 4) else '' for x in self.data['params']]
        rows['mark'] = [yaos[int(x)] for x in self.data['mark']]

        if rows.get('hide'):
            empty = '            '
            rows['hide']['qin6'] = [
                ' %s%s ' % (rows['hide']['qin6'][x], rows['hide']['qinx'][x]) if x in rows['hide']['seat'] else empty
                for x in
                range(0, 6)]
        else:
            rows['hide'] = {'qin6': [' ' for _ in range(0, 6)]}

        #
        if rows.get('bian'):
            if rows['bian']['qin6']:
                rows['bian']['qin6'] = [
                    '%s%s' % (rows['bian']['qin6'][x], rows['bian']['qinx'][x]) if x in self.data['dong'] else '' for x
                    in
                    range(0, 6)]

            if rows['bian']['mark']:
                rows['bian']['mark'] = [x for x in rows['bian']['mark']]
                rows['bian']['mark'] = [yaos[int(rows['bian']['mark'][x])] if x in self.data['dong'] else '' for x in
                                        range(0, 6)]
        else:
            rows['bian'] = {
                'qin6': [' ' for _ in range(0, 6)],
                'mark': [' ' for _ in range(0, 6)],
            }

        shiy = []

        for x in range(0, 6):
            if x == self.data['shiy'][0] - 1:
                shiy.append('世')
            elif x == self.data['shiy'][1] - 1:
                shiy.append('应')
            else:
                shiy.append('  ')

        rows['shiy'] = shiy

        if self.data['guaci']:
            rows['guaci'] = json.load(open(os.path.join(os.path.dirname(__file__), 'data/dd.json'))).get(rows['name'])
            rows['guaci'] = rows['guaci'].replace('********************', "")

        template = Template(tpl)
        return template.render(**rows)

    def export(self):
        solar, params = self.data
        return solar, params

    def predict(self):
        return
