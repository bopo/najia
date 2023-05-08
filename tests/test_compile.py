from najia import Najia
from najia.utils import xkong


def test_compile():
    result = Najia().compile(params=[2, 2, 1, 2, 0, 2], date='2019-12-25 00:20').render()
    assert result


def test_xkong():
    assert xkong('甲子') == '戌亥'
    assert xkong([0, 0]) == '戌亥'
