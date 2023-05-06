from najia.najia import Najia

if __name__ == '__main__':
    params = [2, 2, 1, 2, 4, 2]
    result = Najia(2).compile(params=params, date='2019-12-25 00:20').render()
    print(result)
