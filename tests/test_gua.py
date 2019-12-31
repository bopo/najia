from najia.utils import *

def test_qin6():
    zs = [getQin6('火', constant.ZHI5[constant.ZHIS.index(x[1])]) for x in getNajia('101101')]
    assert getQin6('金', '木') == '妻财'

def test_gong():
    assert getGong("101101", 6) == 2
    # assert palace("101101", 6) == 2

def test_shen6():
    assert getShen6('戊子')[0] == '勾陈'

def test_dong():
    assert setDongYao('101101', 0,2,3,5) == '000000'
    assert setDongYao('101101', 3) == '101001'
    # assert revise('101101', 3) == '101001'
    # assert convert('101101', 3) == '101001'
    # assert transform('101101', 3) == '101001'

def test_xkong():
    assert xkong('甲子') == '戌亥'
    # assert empty('甲子') == '戌亥'

def test_najia():
    assert getNajia('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']
    # assert trunk('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']
    # assert branch('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']
    # assert cycle('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']

def test_progress():
	pass
