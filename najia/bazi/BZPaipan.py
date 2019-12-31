import sys

import sxtwl

import BzBaseClass
from StaticDict import DictClass

type = sys.getfilesystemencoding()


class BzPaipan:
    yZhu = None
    mZhu = None
    dZhu = None
    tZhu = None

    lunar = None

    ySun = None
    mSun = None
    dSun = None
    tSun = None

    yLunar = None
    mLunar = None
    dLunar = None
    tLunar = None

    def __init__(self):
        self.lunar = sxtwl.Lunar()  # 实例化日历库

    def getPaipanbySun(self, y, m, d, t):

        day = self.lunar.getDayBySolar(y, m, d)

        #农历
        self.yLunar = 1984 + day.Lyear0
        self.mLunar = day.Lmc
        self.dLunar = day.Ldi
        self.tLunar = t

        # 找到节气
        jieqilist = day.cur_jq

        #组装干支
        yGan = BzBaseClass.GanClass(day.Lyear2.tg)
        yZhi = BzBaseClass.ZhiClass(day.Lyear2.dz)

        mGan = BzBaseClass.GanClass(day.Lmonth2.tg)
        mZhi = BzBaseClass.ZhiClass(day.Lmonth2.dz)

        dGan = BzBaseClass.GanClass(day.Lday2.tg)
        dZhi = BzBaseClass.ZhiClass(day.Lday2.dz)

        tGanZhi = self.lunar.getShiGz(day.Lday2.tg, t)
        tGan = BzBaseClass.GanClass(tGanZhi.tg)
        tZhi = BzBaseClass.ZhiClass(tGanZhi.dz)

        #组装四柱
        yZhu = BzBaseClass.ZhuClass(yGan, yZhi)
        mZhu = BzBaseClass.ZhuClass(mGan, mZhi)
        dZhu = BzBaseClass.ZhuClass(dGan, dZhi)
        tZhu = BzBaseClass.ZhuClass(tGan, tZhi)

        print("农历", yGan.getGanName(), "年", DictClass.ymc[self.mLunar], "月",
              DictClass.rmc[self.dLunar], "日", tZhi.getZhiName(), "时")

        return BzBaseClass.BZyjClass(yZhu, mZhu, dZhu, tZhu)

    def getPaipanbyLunar(self, y, m, d, t):

        day = self.lunar.getDayByLunar(y, m, d)

        #公历
        self.ySun = day.y
        self.mSun = day.m
        self.dSun = day.d
        self.tSunr = t

        print("公历", self.ySun, "年", self.mSun, "月", self.dSun, "日", "{}时".format(self.tSunr))

        #找到所有节气
        jieqilist = day.cur_jq

        #组装干支
        yGan = BzBaseClass.GanClass(day.Lyear2.tg)
        yZhi = BzBaseClass.ZhiClass(day.Lyear2.dz)

        mGan = BzBaseClass.GanClass(day.Lmonth2.tg)
        mZhi = BzBaseClass.ZhiClass(day.Lmonth2.dz)

        dGan = BzBaseClass.GanClass(day.Lday2.tg)
        dZhi = BzBaseClass.ZhiClass(day.Lday2.dz)

        tGanZhi = self.lunar.getShiGz(day.Lday2.tg, t)
        tGan = BzBaseClass.GanClass(tGanZhi.tg)
        tZhi = BzBaseClass.ZhiClass(tGanZhi.dz)

        #组装四柱
        yZhu = BzBaseClass.ZhuClass(yGan, yZhi)
        mZhu = BzBaseClass.ZhuClass(mGan, mZhi)
        dZhu = BzBaseClass.ZhuClass(dGan, dZhi)
        tZhu = BzBaseClass.ZhuClass(tGan, tZhi)

        return BzBaseClass.BZyjClass(yZhu, mZhu, dZhu, tZhu)
