from najia.utils import xkong


def test_xkong():
    assert xkong('甲子') == '戌亥'
    assert xkong([0, 0]) == '戌亥'
