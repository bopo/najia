from najia.najia import Najia

if __name__ == '__main__':
    # d = {}
    # for k, v in GUA64.items():
    #     i = k[3:] + k[:3]
    #     d[i] = v
    #
    # print(d)
    symbol = [2, 2, 1, 2, 4, 2]
    symbol.reverse()

    gua = Najia()
    ret = gua.compile(symbol=symbol, date='2019-12-25 00:25')
    print(gua.render())
    # gua.render()
