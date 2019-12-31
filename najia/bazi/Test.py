import BzBaseClass
from BZPaipan import BzPaipan
#paipanbySolar(1977,12,7,3)
from BzRules import Bzrules

paipan = BzPaipan()
bzyj = paipan.getPaipanbySun(2002, 12, 25, 8)
bzyj.getPaiPan()

# print(Bzrules.getTgHeshiResult(bzyj.tglist))
# print(Bzrules.getTgChongResult(bzyj.tglist))
# print(Bzrules.getZhiHeResult(bzyj.zhilist))
# print(Bzrules.getZhiChoneResult(bzyj.zhilist))

#bzyj=paipan.getPaipanbyLunar(2002,11,22,8)
#bzyj.getPaiPan();
