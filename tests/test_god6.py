from najia.utils import get_god6


def test_God6():
    """
    【排六神口诀】
     甲乙起青龙 丙丁起朱雀 戊日起勾陈 己日起腾蛇 庚辛起白虎 壬癸起玄武
     1,2      3,4      5         6        7,8      9,10
    :return:
    """

    assert get_god6('甲子')[0] == '青龙'
    assert get_god6('乙丑')[0] == '青龙'
    assert get_god6('丁卯')[0] == '朱雀'
    assert get_god6('丙寅')[0] == '朱雀'


def test_G60():
    assert get_god6('戊卯')[0] == '勾陈'
    assert get_god6('己酉')[0] == '螣蛇'


def test_G61():
    assert get_god6('庚辰')[0] == '白虎'
    assert get_god6('辛巳')[0] == '白虎'

    assert get_god6('壬午')[0] == '玄武'
    assert get_god6('癸未')[0] == '玄武'
