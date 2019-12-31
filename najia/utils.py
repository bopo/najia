import logging
import math

from najia import const

logging.basicConfig(level='INFO')
log = logging.getLogger(__name__)


def getNajia(gz=None):
    return GZ5X(gz)


def GZ5X(gz=''):
    _, z = [i for i in gz]
    zm = const.ZHIS.index(z)
    return gz + const.XING5[const.ZHI5[zm]]


def mark(symbol=None):
    '''
    单拆重交 转 二进制卦码
    :param symbol:
    :return:
    '''
    res = [str(int(x) % 2) for x in symbol]
    log.debug(res)
    return res


def xkong(gz='甲子'):
    '''
    计算旬空
    
    :param gz: 甲子 or 3,11
    :return:
    '''

    gm, zm = [i for i in gz]

    if type(gz) == str:
        gm = const.GANS.index(gm)
        zm = const.ZHIS.index(zm)

    if gm == zm or zm < gm:
        zm += 12

    xk = int((zm - gm) / 2) - 1

    return const.KONG[xk]


def God6(g=0):
    '''
    # 六神, 根据日干五行配对六神五行

    :param g: 日地支
    :return:
    '''

    g, _ = [i for i in g]

    if type(g) is str:
        g = const.GANS.index(g)

    num = math.ceil((g + 1) / 2) - 1
    return const.SHEN6[num:] + const.SHEN6[:num]


'''
寻世诀：
天同二世天变五，地同四世地变初。
本宫六世三世异，人同游魂人变归。

1. 天同人地不同世在二，天不同人地同在五
2. 三才不同世在三
3. 人同其他不同世在四，人不同其他同在三'''


# 世爻初爻是1，二爻是2
# 寻世诀： 天同二世天变五  地同四世地变初  本宫六世三世异  人同游魂人变归
# int('111', 2) => 7
# 世爻 >= 3, 应爻 = 世爻 - 3， index = 5 - 世爻 + 1
# 世爻 <= 3, 应爻 = 世爻 + 3，
# life oneself
def setShiYao(symbol=None):
    '''
    获取世爻

    :param symbol: 卦的二进制码
    :return: 世爻，应爻，所在卦宫位置
    '''
    Wai = symbol[3:]  # 外卦
    Nei = symbol[:3]  # 内卦

    def shiy(shi, index=None):
        ying = shi - 3 if shi >= 3 else shi + 3
        index = shi if index is None else index

        return shi, ying, index

    # 天同二世天变五
    if Wai[2] == Nei[2]:
        if Wai[1] != Nei[1] and Wai[0] != Nei[0]:
            return shiy(2)
    else:
        if Wai[1] == Nei[1] and Wai[0] == Nei[0]:
            return shiy(5)

    # 人同游魂人变归
    if Wai[1] == Nei[1]:
        if Wai[0] != Nei[0] and Wai[2] != Nei[2]:
            return shiy(4, 6)  # , Hun
    else:
        if Wai[0] == Nei[0] and Wai[2] == Nei[2]:
            return shiy(4, 7)  # , Hun

    # 地同四世地变初
    if Wai[0] == Nei[0]:
        if Wai[1] != Nei[1] and Wai[2] != Nei[2]:
            return shiy(4)
    else:
        if Wai[1] == Nei[1] and Wai[2] == Nei[2]:
            return shiy(1)

    # 本宫六世
    if Wai == Nei:
        return shiy(6)

    # 三世异
    return shiy(3)


def palace(symbol=None, index=None):  # inStr -> '111000'  # intNum -> 世爻
    '''
    六爻卦的卦宫名

    认宫诀：
    一二三六外卦宫，四五游魂内变更。
    若问归魂何所取，归魂内卦是本宫。

    :param symbol: 卦的二进制码
    :param index: 世爻
    :return:
    '''

    Wai = symbol[3:]  # 外卦
    Nei = symbol[:3]  # 内卦

    Hun = ''

    if Wai[1] == Nei[1]:
        if Wai[0] != Nei[0] and Wai[2] != Nei[2]:
            Hun = '游魂'
    else:
        if Wai[0] == Nei[0] and Wai[2] == Nei[2]:
            Hun = '归魂'

    # 一二三六外卦宫
    if index in (1, 2, 3, 6):
        return const.YAOS.index(Wai)
    # 归魂内卦是本宫
    elif Hun == '归魂':
        return const.YAOS.index(Nei)
    # 四五游魂内变更
    elif index in (4, 5) or Hun == '游魂':
        symbol = ''.join([str(int(c) ^ 1) for c in Nei])
        return const.YAOS.index(symbol)


# 判断是否六冲卦
# verb
def attack(symbol):
    Wai = symbol[:3]  # 外卦
    Nei = symbol[3:]  # 内卦

    # 内外卦相同
    if Wai == Nei:
        return True

    # 天雷无妄 和 雷天大壮
    if len(set([Nei, Wai]).difference(set(['001', '111']))) == 0:
        return True

    return False


# 纳甲配干支
def getNajia(symbol=None):
    '''
    纳甲配干支

    :param symbol:
    :return:
    '''

    Wai = symbol[3:]  # 外卦
    Nei = symbol[:3]  # 内卦

    log.debug(Wai)
    log.debug(Nei)

    wai, nei = const.YAOS.index(Wai), const.YAOS.index(Nei)

    gan = const.NAJIA[nei][0][0]
    ngz = ['{}{}'.format(gan, zhi) for zhi in const.NAJIA[nei][0][1:]]  # 排干支

    gan = const.NAJIA[wai][1][0]
    wgz = ['{}{}'.format(gan, zhi) for zhi in const.NAJIA[wai][1][1:]]  # 排干支

    log.debug(ngz + wgz)

    return ngz + wgz


def setDongYao(gua, *args):
    yao = set([int(i) for i in args])

    return ''.join([
        str(abs(int(v) - 1)) if int(i) in yao else v for i, v in enumerate(gua)
    ])


def Qin6(w1, w2):
    '''
    两个五行判断六亲
    水1 # 木2 # 金3 # 火4 # 土5

    :param w1:
    :param w2:
    :return:
    '''
    w1 = const.XING5.index(w1) if type(w1) is str else w1
    w2 = const.XING5.index(w2) if type(w2) is str else w2

    ws = w1 - w2
    ws = ws + 5 if ws < 0 else ws
    q6 = const.QING6[ws]
    log.debug(ws)
    log.debug(q6)
    return q6


def guaName(symbol=None):
    symbol = [x for x in symbol]
    symbol.reverse()
    symbol = ''.join(symbol)
    return const.GUA64[symbol]
