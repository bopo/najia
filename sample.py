import sxtwl

from najia.const import *
from najia.utils import (palace, getNajia, Qin6, God6,
                         setShiYao, xkong)


def transform(daily):
    pass


if __name__ == '__main__':
    print('''
男测：测天气

√ 公历：2019年 12月 25日 0时 20分
√ 干支：己亥年 丙子月 丙申日 戊子时 （旬空：辰巳)

得地山谦之水山蹇

青龙          兄弟癸酉金 `` 
玄武          子孙癸亥水 ``世 × 父母戊戌土 `  
白虎          父母癸丑土 `` 
螣蛇          兄弟丙申金 `  
勾陈 妻财丁卯木 官鬼丙午火 ``应
朱雀          父母丙辰土 ``
''')

    lunar = sxtwl.Lunar()
    daily = lunar.getDayBySolar(2019, 12, 25)
    tGanZhi = lunar.getShiGz(daily.Lday2.tg, 0)

    print(
        '{}{}{}'.format(GANS[daily.Lyear2.tg], ZHIS[daily.Lyear2.dz],
                        '年'), '{}{}{}'.format(GANS[daily.Lmonth2.tg],
                                              ZHIS[daily.Lmonth2.dz], '月'),
        '{}{}{}'.format(GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz],
                        '日'), '{}{}{}'.format(GANS[tGanZhi.tg],
                                              ZHIS[tGanZhi.dz], '时'), '旬空:',
        '(%s)' % xkong(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]])))

    # # print(setShiYao('111111'))
    # zs = [setQin6('金', ZHI5[ZHIS.index(x[1])]) for x in setGanZhi('000100')]
    # gong = getGong('000100', setShiYao('000100')[0])

    # print(XING5[GUA5[gong]])
    # print('宫五行', XING5[int(GUA5[gong])])
    # print('卦宫:', GUAS[gong])  # 世6爻
    # print('世爻:', setShiYao('000100'))  # 世6爻
    # print('纳甲:', setGanZhi('000100'))  # 世6爻
    # print('六亲:', zs)  # 世6爻
    # print('六亲:', len(set(zs)))  # 世6爻
    # print('六神:', setShen6(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]])))  # 世6爻

    # # 伏神计算
    # if len(set(zs)) < 5:
    #     gua = YAOS[gong] * 2
    #     qin = [
    #         setQin6(XING5[GUA5[gong]], ZHI5[ZHIS.index(x[1])])
    #         for x in setGanZhi(gua)
    #     ]

    #     print(qin)

    #     naja = setGanZhi(gua)
    #     naj5 = [ZHI5[ZHIS.index(x[-1])] for x in naja]
    #     diff = list(set(qin).difference(set(zs)))
    #     yaos = [qin.index(x) for x in diff]
    #     fush = [naja[i] for i in yaos]
    #     naj5 = [XING5[int(naj5[i])] for i in yaos]

    #     print(diff, yaos, fush, naj5)

    # # 变卦计算
    # gua = '000100'
    # bia = [2, 1, 3]

    # fan = [(str(int(v) ^ 1) if i in bia else v) for i, v in enumerate(gua)]
    # new = ''.join(fan)

    # print(gua)
    # print(new)

    # # 六冲计算
    # print(chong('000000'))
    # print(chong('001001'))
    # print(chong('101101'))
    # print(chong('111001'))
    # print(chong('001111'))

    # # 自动摇卦
    # li = []

    # for x in range(0, 6):
    #     li.append(random.randint(1, 4))

    # # 手动输入
    # li = '1,2,3,4,2,1'.split(',')
    # sb = ['', '`', '``', '○', '×']
    # st = [sb[int(x)] for x in li]

    # print(st)

    # st.reverse()
    # li.reverse()

    # print(st)
    # print(li)

    # print(''.join([str(int(l) % 2) for l in li]))
    # print(GUA64[''.join([str(int(l) % 2) for l in li])])


def guainfo(symbol):
    symbol.reverse()
    print(symbol)

    mark = [str(int(l) % 2) for l in symbol]
    mark = ''.join(mark)

    # print(mark)
    # print('name', GUA640[mark])

    bian = []

    bian = ['1' if v in [1, 4] else '0' for v in symbol]
    bian = ''.join(bian)
    bianN = GUA64[bian]
    # print('bian', GUA64[bian])

    name = GUA64[mark]
    # print('name', GUA64[mark])
    # print('mark', mark)
    # print('bian', bian)
    # print('bian', GUA64[bian])

    # fun1 = [(str(int(y) ^ 1) if x == bian else y) for x, y in enumerate(mark)]
    # print(fun1)
    # bian = ''.join(fun1)

    print('shiy', setShiYao(mark))

    # 卦宫
    gong = palace(mark, setShiYao(mark)[0])
    print('gong', gong)

    # print(name)
    mark = mark
    # print(setShiYao(mark))

    qins6 = [Qin6(XING5[int(GUA5[gong])], ZHI5[ZHIS.index(x[1])]) for x in getNajia('000100')]
    # shen6 = setShen6(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]]))

    gong5x = XING5[int(GUA5[gong])]
    guagong = GUAS[gong]

    shiyao = setShiYao(mark)
    najia = getNajia(mark)

    # print('六亲:', zs)  # 世6爻
    # print('六亲:', len(set(zs)))  # 世6爻

    shen6 = God6(''.join([GANS[daily.Lday2.tg], ZHIS[daily.Lday2.dz]]))

    if len(set(qins6)) < 5:
        fu1 = YAOS[gong] * 2
        fu2 = GUA64[fu1]

    for x in locals().items():
        print(x)

    return {
        'name': name,
        'mark': mark,
        'gong': gong,
        'shiy': shiyao,
        'naja': najia,
        'gold': shen6,
        'qins': qins6,
        'bian': bian,
        # 'fun1': fun1,
        # 'fush': fun1,
    }


if __name__ == '__main__':
    guainfo([2, 2, 1, 2, 4, 2])
