from najia.najia import Najia

if __name__ == '__main__':
    # d = {}
    # for k, v in GUA64.items():
    #     i = k[3:] + k[:3]
    #     d[i] = v
    #
    # print(d)
    params = [2, 2, 1, 2, 4, 2]
    # params.reverse()

    gua = Najia()
    ret = gua.compile(params=params, date='2019-12-25 00:20')
    gua.render()
    # gua.render()
