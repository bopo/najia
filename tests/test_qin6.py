from najia.utils import qin6

'''
# 六亲
QING6 = ("兄弟", "父母", "官鬼", "妻财", "子孙")

# 五行
XING5 = ('木', '火', '土', '金', '水')
'''


def test_qin6():
    assert qin6('金', '木') == '妻财'
    assert qin6('木', '金') == '官鬼'
    assert qin6('金', '水') == '子孙'
    assert qin6('金', '土') == '父母'
    assert qin6('金', '金') == '兄弟'
