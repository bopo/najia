from najia.utils import xkong

'''
KONG = ("子丑", "寅卯", "辰巳", "午未", "申酉", "戌亥")
'''


def test_xkong():
    assert xkong([0, 0]) == '戌亥'

    assert xkong('甲子') == '戌亥'
    assert xkong('甲戌') == '申酉'
    assert xkong('甲申') == '午未'
    assert xkong('甲午') == '辰巳'
    assert xkong('甲辰') == '寅卯'
    assert xkong('甲寅') == '子丑'
