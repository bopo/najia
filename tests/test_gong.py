# 六爻卦的卦宫名
from najia import const


def GuaGong(inStr, intNum):  # inStr -> '111000'  # intNum -> 世爻
    Nei = inStr[:3]  # 外卦
    Wai = inStr[3:]  # 内卦
    Hun = ''

    if Wai[1] == Nei[1]:
        if Wai[0] != Nei[0] and Wai[2] != Nei[2]:
            Hun = '游魂'
    else:
        if Wai[0] == Nei[0] and Wai[2] == Nei[2]:
            Hun = '归魂'

    # 一二三六外卦宫
    if intNum in (1, 2, 3, 6):
        return const.YAOS.index(Wai)
    # 归魂内卦是本宫
    elif Hun == '归魂':
        return const.YAOS.index(Nei)
    # 四五游魂内变更
    elif intNum in (4, 5) or Hun == '游魂':
        symbol = ''.join([str(int(c) ^ 1) for c in Nei])
        return const.YAOS.index(symbol)


if __name__ == '__main__':
    print(GuaGong('001000', 4))
