from najia.utils import mark


def test_mark():
    symbol = [2, 2, 1, 2, 4, 2]

    assert mark(symbol) == ['0', '0', '1', '0', '0', '0']
    assert mark(''.join([str(x) for x in symbol])) == ['0', '0', '1', '0', '0', '0']
