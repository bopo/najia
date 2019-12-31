'''
计算干支的刑冲合害
'''
from BZBaseTools import BZBaseTools
from StaticDict import DictClass


class Bzrules:
    res_rulus = None

    #判断天干六合：tg1-tg2的绝对值的5，则合。
    #输入参数为天干的数组，输出为六合与合化的结果
    # #判断rule1_tghe结果是否有效，即合化否，如果合化则增加权重。
    def getTgHe(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "".join(keys)
            if DictClass.TgHe.__contains__(vv):
                result.append(DictClass.TgHe.get(vv))
        return result

    #0甲6庚相冲、1乙7辛相冲、8壬2丙相冲、9癸3丁相冲，5戊4己土居中央，故无冲
    #甲属阳木，为东方，庚属阳金，为西方，阳与阳同类相斥，金与木相克，而且二者方位相反，故曰相冲。其余之干相冲类推。
    def getTgChong(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "".join(keys)
            if DictClass.TgChong.__contains__(vv):
                result.append(DictClass.TgChong.get(vv))
        return result

    #0甲克5戊，1乙克4己、5戊克8壬，4己克9癸、8壬克2丙，9癸克3丁、2丙克6庚，3丁克7辛、6庚克0甲，7辛克1乙
    #注意是有方向性的
    def getTgKe(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "".join(keys)
            if DictClass.Tgke.__contains__(vv):
                result.append(DictClass.Tgke.get(vv))
        return result

    #地支六合===========
    #0子1丑合化土,2寅11亥合化木,3卯10戌合化火,4辰9酉合化金,5巳8申合化水,6午7未合,化土化土
    def getZhiHe(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiHe.__contains__(vv):
                result.append(DictClass.ZhiHe.get(vv))
        return result

    #地支六冲==========
    #0子6午相冲、1丑7未相冲、2寅8申相冲、3卯9酉相冲、4辰10戌相冲、5巳11亥相冲
    def getZhiChong(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiChong.__contains__(vv):
                result.append(DictClass.ZhiChong.get(vv))
        return result

    #地支三合 2寅6午10戌三合火;8申0子4辰三合水;11亥3卯7未三合木;5巳9酉1丑三合金;
    def getZhiSanhe(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 3)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiSanhe.__contains__(vv):
                result.append(DictClass.ZhiSanhe.get(vv))
        return result

    #地支半合，如果三合成立，则将结果集中去掉半合,输入三合结果集,
    def getZhiSanheban(sanheResult, L):
        result = []
        if len(sanheResult) > 0:
            tool = BZBaseTools()
            res = tool.Combinations(L, 2)
            n = len(res)
            for i in range(n):
                # 把int list转化为str内容的list
                keys = map(str, res[i])
                vv = "-".join(keys)
                if DictClass.ZhiSanheban.__contains__(vv):
                    result.append(DictClass.ZhiSanheban.get(vv))

        return result

    #地支三会 11亥0子1丑北方三会水；2寅3卯4辰东方三会木；5巳6午7未南方三会火；8申9酉10戌西方三会金
    def getZhiSanhui(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 3)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiSanhui.__contains__(vv):
                result.append(DictClass.ZhiSanhui.get(vv))
        return result

    #地支相刑（有方向） 7未刑1丑、1丑刑10戌、10戌刑7未，为无恩之刑；2寅刑5巳、5巳刑8申、8申刑2寅，为恃势之刑；0子刑3卯、3卯刑0子，为无礼之刑；44辰、66午、99酉、11亥自刑。
    def getZhiXiangxing(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiXiangxing.__contains__(vv):
                result.append(DictClass.ZhiXiangxing.get(vv))
        return result

    #地支相害（无方向） 0子7未相害、1丑6午相害、2寅5巳相害、3卯4辰相害、8申11亥相害、9酉10戌相害
    def getZhiXianghai(L):
        result = []
        tool = BZBaseTools()
        res = tool.Combinations(L, 2)
        n = len(res)
        for i in range(n):
            # 把int list转化为str内容的list
            keys = map(str, res[i])
            vv = "-".join(keys)
            if DictClass.ZhiXianghai.__contains__(vv):
                result.append(DictClass.ZhiXianghai.get(vv))

        #result中没有去掉重复的
        return result


if __name__ == '__main__':
    l = [2, 6, 10]
    print("===tiangan===")
    print(Bzrules.getTgHe(l))
    print(Bzrules.getTgChong(l))
    print(Bzrules.getTgKe(l))
    print("===dizhi===")

    print(Bzrules.getZhiHe(l))
    print(Bzrules.getZhiChong(l))
    print(Bzrules.getZhiXianghai(l))
    print(Bzrules.getZhiXiangxing(l))
    print(Bzrules.getZhiSanhe(l))
    # print(Bzrules.getZhiSanheban(l))
    print(Bzrules.getZhiSanhui(l))
