'''
干支的相关计算
'''

from BZBaseTools import BZBaseTools
from StaticDict import DictClass


class GanClass:
    ganid = 0

    def __init__(self, ganid):
        self.ganid = ganid

    #获得十神名称,注意此方法为，自身天干是对方的什么十神，即需要输入的是日干，得出的结果是针对日干的十神
    def getSSName(self, tgid):
        return DictClass.ShishenName[BZBaseTools.ShishenList[tgid][self.ganid]]

    def getGanName(self):
        return DictClass.Gan[self.ganid]

    def getWuxingName(self):
        return DictClass.Wuxing[self.ganid]

    def getWuxingshengwang(self, zhiid):
        id = BZBaseTools.WuxingShengwang[zhiid][BZBaseTools.ganwuxing[
            self.ganid]]
        return DictClass.WuxingShengwangName[id]


class GanYangClass(GanClass):
    yinyang = "阳"


class GanYinClass(GanClass):
    yinyang = "阴"


class ZhiClass:
    zhiid = 0

    def __init__(self, zhiid):
        self.zhiid = zhiid

    def getZhiName(self):
        return DictClass.Zhi[self.zhiid]

    def getZhiingan(self):
        return BZBaseTools.DzinTg[self.zhiid]

    def getZhiinganname(self):
        list = []
        for x in BZBaseTools.DzinTg[self.zhiid]:
            list.append(DictClass.Gan[x])
        return list

    def getJijie(self):
        id = BZBaseTools.Jijie[self.zhiid]
        return DictClass.Jijie[id]


class ZhiYangClass(GanClass):
    yinyang = "阳"


class ZhiYinClass(GanClass):
    yinyang = "阴"


#单柱
class ZhuClass:
    tiangan = None
    dizhi = None

    def __init__(self, tigan, dizhi):
        self.tiangan = tigan
        self.dizhi = dizhi

    #得到本柱天干十二长生宫
    def getShierchangshengName(self, tg, dz):
        id = BZBaseTools.Shierchangsheng[tg.ganid][dz.zhiid]
        return DictClass.ShierchangshengName[id]

    #得到本柱的纳音
    def getNayin(self):
        return DictClass.Nayin[self.tiangan.getGanName() +
                               self.dizhi.getZhiName()]

    #得到本柱的旬首
    """
    地支—天干=旬首常数(甲子0;甲寅2;甲辰4;甲午6;甲申8;甲戌10)
    例如求辛巳的旬首,用地支(巳)的序号6减去天干(辛)的序号8(地支小于天干时加12),得10。所以得旬首甲戌
    """
    def getXunshou(self):
        ganid = self.tiangan.ganid
        zhiid = self.dizhi.zhiid

        if zhiid < ganid:
            zhiid = zhiid + 12

        ret = zhiid - ganid

        if ret == 0:
            return "甲子"
        elif ret == 2:
            return "甲寅"
        elif ret == 4:
            return "甲辰"
        elif ret == 6:
            return "甲午"
        elif ret == 8:
            return "甲申"
        elif ret == 10:
            return "甲戌"
        else:
            return ""

    """
    旬空查法:地支数-天干数=空亡数
    (0或12戌亥,2子丑,4寅卯,6辰巳,8午未,10申酉)即将“地支”减“天干”即可。若不够减,加12再减。得数必是双数,加上前面的单数即可(因每旬“空亡”有两天)。
    若减后得数为2,必是子、丑空,为4,必是寅、卯空,为6,必是辰、巳空。例如“丙辰”日,辰5-丙3=2丑,即子、丑空。
    又如“壬申”日,壬9-申9=0,即戌、亥空。又如“辛丑”日,丑2-辛8不够减,加12再减,即2+12-8=6,6即辰、巳空
    """

    #得到本柱的旬空
    def getXunkong(self):
        ganid = self.tiangan.ganid
        zhiid = self.dizhi.zhiid
        if zhiid <= ganid:
            zhiid = zhiid + 12

        ret = zhiid - ganid
        
        if ret == 2:
            return "子丑"
        elif ret == 4:
            return "寅卯"
        elif ret == 6:
            return "辰巳"
        elif ret == 8:
            return "午未"
        elif ret == 10:
            return "申酉"
        elif ret == 12:
            return "戌亥"
        else:
            return ""


#八字原局
class BZyjClass:
    yZhu = None
    mZhu = None
    dZhu = None
    tZhu = None
    tglist = None
    zhilist = None

    def __init__(self, yZhu, mZhu, dZhu, tZhu):
        self.yZhu = yZhu
        self.mZhu = mZhu
        self.dZhu = dZhu
        self.tZhu = tZhu

        self.tglist = [
            yZhu.tiangan.ganid, mZhu.tiangan.ganid, dZhu.tiangan.ganid,
            tZhu.tiangan.ganid
        ]
        self.zhilist = [
            yZhu.dizhi.zhiid, mZhu.dizhi.zhiid, dZhu.dizhi.zhiid,
            tZhu.dizhi.zhiid
        ]

    def getPaiPan(self):
        print(
            "年：" + self.yZhu.tiangan.getGanName() + " " +
            self.yZhu.dizhi.getZhiName(), self.yZhu.getNayin(), "旬空:",
            self.yZhu.getXunkong())

        print(
            "月：" + self.mZhu.tiangan.getGanName() + " " +
            self.mZhu.dizhi.getZhiName(), self.mZhu.getNayin(), "旬空:",
            self.mZhu.getXunkong())

        print(
            "日：" + self.dZhu.tiangan.getGanName() + " " +
            self.dZhu.dizhi.getZhiName(), self.dZhu.getNayin(), "旬空:",
            self.dZhu.getXunkong())

        print(
            "时：" + self.tZhu.tiangan.getGanName() + " " +
            self.tZhu.dizhi.getZhiName(), self.tZhu.getNayin(), "旬空:",
            self.tZhu.getXunkong())

        print("年十神：" + self.yZhu.tiangan.getSSName(self.dZhu.tiangan.ganid))
        print("月十神：" + self.mZhu.tiangan.getSSName(self.dZhu.tiangan.ganid))
        print("时十神：" + self.tZhu.tiangan.getSSName(self.dZhu.tiangan.ganid))
