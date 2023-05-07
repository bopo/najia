import logging
import math

from . import const

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def gz5_x(gz=''):
    """
    干支五行
    :param gz:
    :return:
    """
    _, z = [i for i in gz]
    zm = const.ZHIS.index(z)

    return gz + const.XING5[const.ZHI5[zm]]


def mark(symbol=None):
    """
    单拆重交 转 二进制卦码
    :param symbol:
    :return:
    """

    res = [str(int(x) % 2) for x in symbol]
    logger.debug(res)

    return res


def xkong(gz='甲子'):
    """
    计算旬空

    :param gz: 甲子 or 3,11
    :return:
    """

    gm, zm = [i for i in gz]

    if type(gz) == str:
        gm = const.GANS.index(gm)
        zm = const.ZHIS.index(zm)

    if gm == zm or zm < gm:
        zm += 12

    xk = int((zm - gm) / 2) - 1

    return const.KONG[xk]


def god6(gz=None):
    """
    # 六神, 根据日干五行配对六神五行

    :param gz: 日干支
    :return:
    """

    gm, _ = [i for i in gz]

    if type(gm) is str:
        gm = const.GANS.index(gm)

    num = math.ceil((gm + 1) / 2) - 7

    if gm == 4:
        num = -4

    if gm == 5:
        num = -3

    if gm > 5:
        num += 1

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
def set_shi_yao(symbol=None):
    """
    获取世爻

    :param symbol: 卦的二进制码
    :return: 世爻，应爻，所在卦宫位置
    """
    wai = symbol[3:]  # 外卦
    nei = symbol[:3]  # 内卦

    def shiy(shi, index=None):
        ying = shi - 3 if shi > 3 else shi + 3
        index = shi if index is None else index
        return shi, ying, index

    # 天同二世天变五
    if wai[2] == nei[2]:
        if wai[1] != nei[1] and wai[0] != nei[0]:
            return shiy(2)
    else:
        if wai[1] == nei[1] and wai[0] == nei[0]:
            return shiy(5)

    # 人同游魂人变归
    if wai[1] == nei[1]:
        if wai[0] != nei[0] and wai[2] != nei[2]:
            return shiy(4, 6)  # , Hun
    else:
        # fix 归魂问题
        if wai[0] == nei[0] and wai[2] == nei[2]:
            return shiy(3, 6)  # , Hun

    # 地同四世地变初
    if wai[0] == nei[0]:
        if wai[1] != nei[1] and wai[2] != nei[2]:
            return shiy(4)
    else:
        if wai[1] == nei[1] and wai[2] == nei[2]:
            return shiy(1)

    # 本宫六世
    if wai == nei:
        return shiy(6)

    # 三世异
    return shiy(3)


def get_type(symbol=None):
    if res := soul(symbol):
        return res

    if attack(symbol):
        return '六冲'

    if res := unite(symbol):
        return res

    return ''


def unite(symbol=None):
    name = const.GUA64[symbol]

    for x in const.LIUHE:
        if x in name:
            return '六合'

    return None


def soul(symbol=None):
    wai = symbol[3:]  # 外卦
    nei = symbol[:3]  # 内卦
    hun = ''

    if wai[1] == nei[1]:
        if wai[0] != nei[0] and wai[2] != nei[2]:
            hun = '游魂'
    else:
        if wai[0] == nei[0] and wai[2] == nei[2]:
            hun = '归魂'

    return hun


def palace(symbol=None, index=None):  # inStr -> '111000'  # intNum -> 世爻
    """
    六爻卦的卦宫名

    认宫诀：
    一二三六外卦宫，四五游魂内变更。
    若问归魂何所取，归魂内卦是本宫。

    :param symbol: 卦的二进制码
    :param index: 世爻
    :return:
    """

    wai = symbol[3:]  # 外卦
    nei = symbol[:3]  # 内卦
    hun = ''

    if wai[1] == nei[1]:
        if wai[0] != nei[0] and wai[2] != nei[2]:
            hun = '游魂'
    else:
        if wai[0] == nei[0] and wai[2] == nei[2]:
            hun = '归魂'

    # 归魂内卦是本宫
    if hun == '归魂':
        return const.YAOS.index(nei)

    # 一二三六外卦宫
    if index in (1, 2, 3, 6):
        return const.YAOS.index(wai)

    # 四五游魂内变更
    if index in (4, 5) or hun == '游魂':
        symbol = ''.join([str(int(c) ^ 1) for c in nei])
        return const.YAOS.index(symbol)


# 判断是否六冲卦
# verb
def attack(symbol):
    wai = symbol[3:]  # 外卦
    nei = symbol[:3]  # 内卦

    # 内外卦相同
    if wai == nei:
        return True

    # 天雷无妄 和 雷天大壮
    gua = [nei, wai]

    try:
        if len(set(gua).difference(('100', '111'))) == 0:
            return True
    except TypeError:
        pass

    return False


# 纳甲配干支
def get_najia(symbol=None):
    """
    纳甲配干支

    :param symbol:
    :return:
    """

    wai = symbol[3:]  # 外卦
    nei = symbol[:3]  # 内卦

    wai, nei = const.YAOS.index(wai), const.YAOS.index(nei)

    gan = const.NAJIA[nei][0][0]
    ngz = [f'{gan}{zhi}' for zhi in const.NAJIA[nei][0][1:]]  # 排干支

    gan = const.NAJIA[wai][1][0]
    wgz = [f'{gan}{zhi}' for zhi in const.NAJIA[wai][1][1:]]  # 排干支

    return ngz + wgz


def qin6(w1, w2):
    """
    两个五行判断六亲
    水1 # 木2 # 金3 # 火4 # 土5

    :param w1:
    :param w2:
    :return:
    """
    w1 = const.XING5.index(w1) if type(w1) is str else w1
    w2 = const.XING5.index(w2) if type(w2) is str else w2

    ws = w1 - w2
    ws = ws + 5 if ws < 0 else ws
    q6 = const.QING6[ws]

    logger.debug(ws)
    logger.debug(q6)

    return q6
