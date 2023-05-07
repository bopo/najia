from najia.utils import GZ5X

'''
# 六亲
QING6 = ("兄弟", "父母", "官鬼", "妻财", "子孙")

# 五行
XING5 = ('木', '火', '土', '金', '水')
'''


def test_gzwx():
    assert GZ5X('甲子') == '甲子水'
