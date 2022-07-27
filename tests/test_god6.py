from najia.utils import God6


def test_God6():
    """
    【排六神口诀】
     甲乙起青龙 丙丁起朱雀 戊日起勾陈 己日起腾蛇 庚辛起白虎 壬癸起玄武
     12        34       5         6       78        9,10
    :return:
    """

    assert God6('甲子')[0] == '青龙'
    assert God6('乙丑')[0] == '青龙'
    assert God6('丁卯')[0] == '朱雀'
    assert God6('丙寅')[0] == '朱雀'


def test_G60():
    assert God6('戊卯')[0] == '勾陈'
    assert God6('己酉')[0] == '螣蛇'


def test_G61():
    assert God6('庚辰')[0] == '白虎'
    assert God6('辛巳')[0] == '白虎'

    assert God6('壬午')[0] == '玄武'
    assert God6('癸未')[0] == '玄武'
