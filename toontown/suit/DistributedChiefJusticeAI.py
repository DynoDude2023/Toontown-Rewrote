#make a class that inherits from DistributedLawbotBossAI

from direct.directnotify import DirectNotifyGlobal
import DistributedLawbotBossAI
from toontown.toonbase import ToontownGlobals

class DistributedChiefJusticeAI(DistributedLawbotBossAI.DistributedLawbotBossAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedChiefJusticeAI')
    
    def __init__(self, air, star):
        DistributedLawbotBossAI.DistributedLawbotBossAI.__init__(self, air)
        
        if star == 1:
            self.lawyerDNA = ['bf', 'b', 'dt']
            self.damageMult = 0.8
            self.suitPlannerNumber = 13
        elif star == 2:
            self.lawyerDNA = ['b', 'dt', 'ac']
            self.damageMult = 1.4
            self.suitPlannerNumber = 18
        elif star == 3:
            self.lawyerDNA = ['dt', 'ac', 'bs', 'sd']
            self.damageMult = 1.8
            self.suitPlannerNumber = 19
        elif star == 4:
            self.lawyerDNA = ['ac', 'bs', 'sd', 'le']
            self.damageMult = 2.2
            self.suitPlannerNumber = 20
        elif star == 5:
            self.lawyerDNA = ['bs', 'sd', 'le', 'bw']
            self.damageMult = 3.0
            self.suitPlannerNumber = 21