from najia.utils import get_najia


def test_najia():
    assert get_najia('101101') == ['己卯', '己丑', '己亥', '己酉', '己未', '己巳']
