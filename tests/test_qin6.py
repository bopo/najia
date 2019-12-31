from najia import const
from najia.utils import Qin6, getNajia


def test_qin6():
    zs = [Qin6('火', const.ZHI5[const.ZHIS.index(x[1])]) for x in getNajia('101101')]
    assert Qin6('金', '木') == '妻财'
