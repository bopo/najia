from najia.utils import getNajia


def test_najia():
    assert getNajia('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']
