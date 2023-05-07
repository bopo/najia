'''
# 六亲
QING6 = ("兄弟", "父母", "官鬼", "妻财", "子孙")

# 五行
XING5 = ('木', '火', '土', '金', '水')
'''
import pickle


def test_guaci():
    gc = pickle.load(open('najia/data/gc.pkl', 'rb'))

    print(gc.get('乾为天'))
