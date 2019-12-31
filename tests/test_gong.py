# 六爻卦的卦宫名
from najia.utils import getGong


def test_gong():
    assert getGong("101101", 6) == 2
    # assert palace("101101", 6) == 2
