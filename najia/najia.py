# -*- coding: utf-8 -*-

import logging

import arrow
import sxtwl
from jinja2 import Template

from najia.const import GANS, ZHIS, GUA64, XING5, GUA5, ZHI5, YAOS
from najia.utils import (palace, getNajia, Qin6, God6,
                         setShiYao, xkong, GZ5X)

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


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

    def _hidden(self, gong=None, qins=None):
        '''
        计算伏神卦

        :param gong:
        :param qins:
        :return:
        '''
        if gong is None:
            raise Exception('')

        if qins is None:
            raise Exception('')

        if len(set(qins)) < 5:
            mark = YAOS[gong] * 2
            logger.debug(mark)
            qin6 = [(Qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])])) for x in getNajia(mark)]
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

    def _transform(self, params=None):
        '''
        计算变卦

        :param params:
        :return:
        '''

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

    def compile(self, params=None, gender=1, date=None, title=None):
        '''
        根据参数编译卦

        :param params:
        :param date:
        :return:
        '''
        lunar = self._daily(date)
        solar = arrow.get(date)
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
        # exit()

        # 伏神
        hide = self._hidden(gong, qin6)

        # 变卦
        # params.reverse()
        bian = self._transform(params=params)

        self.data = {
            'params': params,
            'gender': gender,
            'title': title,
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
            'hide': hide
        }

        logger.debug(self.data)

        return self

    def render(self):
        '''

        :return:
        '''

        demo = '''{{gender}}测：测天气

√ 公历：2019年 12月 25日 0时 20分
√ 干支：己亥年 丙子月 丙申日 戊子时 （旬空：辰巳)

得「地山谦」之「水山蹇」

青龙          兄弟癸酉金 `` 
玄武          子孙癸亥水 ``世 × 父母戊戌土 `  
白虎          父母癸丑土 `` 
螣蛇          兄弟丙申金 `  
勾陈 妻财丁卯木 官鬼丙午火 ``应
朱雀          父母丙辰土 ``
'''
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
'''
        rows = self.data
        yaos = ['``', '` ', '``', '○', '×']

        rows['dyao'] = [yaos[x] if x in (3, 4) else '' for x in self.data['params']]
        rows['mark'] = [yaos[int(x)] for x in self.data['mark']]

        if rows.get('hide'):
            empty = '            '
            rows['hide']['qin6'] = [
                ' %s%s ' % (rows['hide']['qin6'][x], rows['hide']['qinx'][x]) if x in rows['hide']['seat'] else empty
                for x in
                range(0, 6)]
        else:
            rows['hide']= {'qin6': [' ' for _ in range(0, 6)]}

        #
        if rows.get('bian'):
            if rows['bian']['qin6']:
                rows['bian']['qin6'] = [
                    '%s%s' % (rows['bian']['qin6'][x], rows['bian']['qinx'][x]) if x in self.data['dong'] else '' for x in
                    range(0, 6)]

            if rows['bian']['mark']:
                rows['bian']['mark'] = [x for x in rows['bian']['mark']]
                rows['bian']['mark'] = [yaos[int(rows['bian']['mark'][x])] if x in self.data['dong'] else '' for x in
                                        range(0, 6)]
        else:
            rows['bian']= {
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

        template = Template(tpl)
        return template.render(**rows)

    def export(self):
        solar, params = self.data
        return solar, params

    def predict(self):
        return
