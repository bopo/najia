from najia.utils import Qin6

'''
# 六亲
QING6 = ("兄弟", "父母", "官鬼", "妻财", "子孙")

# 五行
XING5 = ('木', '火', '土', '金', '水')
'''


def test_qin6():
    assert Qin6('金', '木') == '妻财'
    assert Qin6('木', '金') == '官鬼'
    assert Qin6('金', '水') == '子孙'
    assert Qin6('金', '土') == '父母'
    assert Qin6('金', '金') == '兄弟'
