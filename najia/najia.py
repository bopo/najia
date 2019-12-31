# -*- coding: utf-8 -*-

import arrow
import sxtwl
from jinja2 import Template

from najia.const import GANS, ZHIS, GUA64, XING5, GUA5, ZHI5, YAOS
from najia.utils import (getGong, getNajia, getQin6, getShen6,
                         setShiYao, xkong, getGZ5)


class Najia(object):
    """docstring for Najia"""
    bian = None  # 变卦
    hide = None  # 伏神
    data = None

    def _gz(self, cal):
        return GANS[cal.tg] + ZHIS[cal.dz]

    def _cn(self, cal):
        return GANS[cal.tg] + ZHIS[cal.dz]

    def _daily(self, date=None):
        date = arrow.get(date)

        lunar = sxtwl.Lunar()
        daily = lunar.getDayBySolar(date.year, date.month, date.day)
        hour = lunar.getShiGz(daily.Lday2.tg, 0)

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

    def _fu(self, gong=None, qins=None):
        if gong is None:
            raise Exception('')

        if qins is None:
            raise Exception('')

        if len(set(qins)) < 5:
            mark = YAOS[gong] * 2
            qin6 = [(getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(mark)]
            qinx = [getGZ5(x) for x in getNajia(mark)]
            seat = [qin6.index(x) for x in list(set(qin6).difference(set(qins)))]

            return {
                'name': GUA64.get(mark),
                'mark': mark,
                'qin6': qin6,
                'qinx': qinx,
                'seat': seat,
            }

    def _bian(self, symbol=None):
        # 判断变爻
        if symbol is None:
            raise Exception('')

        if type(symbol) == str:
            symbol = [x for x in symbol]

        if len(symbol) < 6:
            raise Exception('')

        symbol.reverse()

        mark = ''.join([str(int(l) % 2) for l in symbol])

        if 3 in symbol or 4 in symbol:
            bian = ''.join(['1' if v in [1, 4] else '0' for v in symbol])
            gong = getGong(mark, setShiYao(mark)[0])  # 卦宫
            qin6 = [(getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(bian)]
            qinx = [getGZ5(x) for x in getNajia(bian)]

            return {
                'name': GUA64.get(mark),
                'mark': mark,
                'qin6': qin6,
                'qinx': qinx,
            }

    def compile(self, symbol=None, date=None):
        lunar = self._daily(date)
        solar = arrow.get(date)

        # 卦码
        mark = ''.join([str(int(l) % 2) for l in symbol])

        # 判断变爻
        if 3 in symbol or 4 in symbol:
            bian = ''.join(['1' if v in [1, 4] else '0' for v in symbol])
            biag = getGong(mark, setShiYao(mark)[0])  # 卦宫
            qinb = [(getQin6(XING5[int(GUA5[biag])], ZHI5[ZHIS.index(x[1])]) + getGZ5(x)) for x in getNajia(bian)]
        else:
            bian = None
            qinb = None

        # 卦宫
        gong = getGong(mark, setShiYao(mark)[0])  # 卦宫

        # 卦名
        name = GUA64[mark]

        # 六亲
        qin6 = [(getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])]) + getGZ5(x)) for x in getNajia(mark)]
        qin6x = [getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])]) for x in getNajia(mark)]

        # 世应爻
        shiy = setShiYao(mark)

        # 六神
        god6 = getShen6(''.join([GANS[lunar['day'].tg], ZHIS[lunar['day'].dz]]))

        godf = None
        qinf = None
        seat = None

        if len(set(qin6x)) < 5:
            godf = YAOS[gong] * 2
            qinf = [(getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])]) + getGZ5(x)) for x in getNajia(godf)]
            qinfx = [(getQin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(godf)]
            fspos = list(set(qinfx).difference(set(qin6x)))
            print(qinfx.index(fspos[0]))
            seat = [qinfx.index(x) for x in fspos]
            print(seat)

        symbol.reverse()

        self.data = {
            'solar': solar,
            'lunar': lunar,
            'symbol': symbol,
            'name': name,
            'mark': mark,
            'gong': gong,
            'shiy': shiy,
            'god6': god6,
            'qin6': qin6,
            'dong': [i for i, x in enumerate(symbol) if x > 2],
            'bian': {'mark': bian, 'qin6': qinb, 'name': GUA64.get(bian)},
            'fu': {'mark': godf, 'qin6': qinf, 'name': GUA64.get(godf), 'seat': seat},
        }

        dong = [i for i, x in enumerate(symbol) if x > 2]
        self.data = {
            'symbol': symbol,
            'title': '',
            'solar': solar,
            'lunar': lunar,
            'god6': god6,
            'dong': dong,
            'name': name,
            'mark': mark,
            'gong': gong,
            'shiy': shiy,
            'qin6': qin6,
            'bian': self._bian(symbol=symbol),
            'fu': self._fu(gong, qin6x)
        }

        print(self.data)

        return self

    def render(self):
        '''

        :return:
        '''
        tpl = '''
男测：{{desc}}

公历：{{solar.year}}年 {{solar.month}}月 {{solar.day}}日 {{solar.hour}}时 {{solar.minute}}分
干支：{{lunar.gz.year}}年 {{lunar.gz.month}}月 {{lunar.gz.day}}日 {{lunar.gz.hour}}时 （旬空：{{lunar.xkong}})

得{{name}}之{{bian.name}}卦

{{god6.5}}{{fu.qin6.5}}{{qin6.5}} {{mark.5}} {{shiy.5}} {{dyao.5}} {{bian.qin6.5}} {{bian.mark.5}}
{{god6.4}}{{fu.qin6.4}}{{qin6.4}} {{mark.4}} {{shiy.4}} {{dyao.4}} {{bian.qin6.4}} {{bian.mark.4}}
{{god6.3}}{{fu.qin6.3}}{{qin6.3}} {{mark.3}} {{shiy.3}} {{dyao.3}} {{bian.qin6.3}} {{bian.mark.3}}
{{god6.2}}{{fu.qin6.2}}{{qin6.2}} {{mark.2}} {{shiy.2}} {{dyao.2}} {{bian.qin6.2}} {{bian.mark.2}}
{{god6.1}}{{fu.qin6.1}}{{qin6.1}} {{mark.1}} {{shiy.1}} {{dyao.1}} {{bian.qin6.1}} {{bian.mark.1}}
{{god6.0}}{{fu.qin6.0}}{{qin6.0}} {{mark.0}} {{shiy.0}} {{dyao.0}} {{bian.qin6.0}} {{bian.mark.0}}
'''
        rows = self.data
        yaos = ['``', '`', '``', '○', '×']

        rows['dyao'] = [yaos[x] if x in (3, 4) else '' for x in self.data['symbol']]
        rows['mark'] = [yaos[int(x)] for x in self.data['mark']]
        rows['mark'].reverse()

        if rows['fu']['qin6']:
            empty = '            '
            rows['fu']['qin6'] = [
                ' %s%s ' % (rows['fu']['qin6'][x], rows['fu']['qinx'][x]) if x in rows['fu']['seat'] else empty for x in
                range(0, 6)]
        else:
            rows['fu']['qin6'] = ['' for _ in range(0, 6)]

        if rows['bian']['qin6']:
            rows['bian']['qin6'] = [
                '%s%s' % (rows['bian']['qin6'][x], rows['bian']['qinx'][x]) if x in self.data['dong'] else '' for x in
                range(0, 6)]

        if rows['bian']['mark']:
            rows['bian']['mark'] = [x for x in rows['bian']['mark']]
            rows['bian']['mark'].reverse()
            rows['bian']['mark'] = [yaos[int(rows['bian']['mark'][x])] if x in self.data['dong'] else '' for x in
                                    range(0, 6)]
        else:
            rows['bian']['mark'] = ['' for _ in range(0, 6)]

        shiy = []

        for x in range(0, 6):
            if x == self.data['shiy'][0] - 1:
                shiy.append('世')
            elif x == self.data['shiy'][1] - 1:
                shiy.append('应')
            else:
                shiy.append('  ')

        rows['shiy'] = shiy

        template = Template(tpl)
        return template.render(**rows)

    def export(self):
        today, symbol = self.data
        return today, symbol

    def predict(self):
        return
