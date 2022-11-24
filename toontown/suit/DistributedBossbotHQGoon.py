#make a class that inherits from DistributedGoon called DistributedBossbotHQGoon

from direct.directnotify import DirectNotifyGlobal
import DistributedGoon
from direct.interval.IntervalGlobal import *
from panda3d.core import *

class DistributedBossbotHQGoon(DistributedGoon.DistributedGoon):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBossbotHQGoon')
    STUN_TIME = 4
    
    def __init__(self, cr, type = 'sg'):        
        DistributedGoon.DistributedGoon.__init__(self, cr)
        self.scale = 2.5
        self.entId = None
        self.goonType = type
        self.goonWalkIntervalPart = None
        
    def generate(self):
        DistributedGoon.DistributedGoon.generate(self)
        return
    
    def setEntId(self, entId):
        self.entId = entId
        self.entIdtoPath = {0: self.goonWalkInterval,
                            1: self.goonWalkInterval1,
                            2: self.goonWalkInterval2,
                            3: self.goonWalkInterval3,
                            4: self.goonWalkInterval4}
        
        self.goonWalkIntervalPart = self.entIdtoPath[self.entId]
        self.goonWalkIntervalPart.loop()
    
    def getEntId(self):
        return self.entId
    
    def enterBattle(self, avId = None, ts = 0):
        DistributedGoon.DistributedGoon.enterBattle(self, avId, ts)
        stopWalkSeq = Sequence(Func(self.goonWalkIntervalPart.pause), Wait(4), Func(self.goonWalkIntervalPart.resume)).start()
    
    def enterStunned(self, ts = 0):
        DistributedGoon.DistributedGoon.enterStunned(self, ts)
        stopWalkSeq = Sequence(Func(self.goonWalkIntervalPart.pause), Wait(4), Func(self.goonWalkIntervalPart.resume)).start()

    def announceGenerate(self):
        DistributedGoon.DistributedGoon.announceGenerate(self)

        if self.entId == 0:
            self.setPos(284, 19.0, 0.025)
        elif self.entId == 1:
            self.setPos(84, 140.0, 0.025)
        elif self.entId == 2:
            self.setPos(-236, -105.0, 3.925)
        elif self.entId == 3:
            self.setPos(4, -207.0, 0.025)
        elif self.entId == 4:
            self.setPos(-206, 210.0, 3.925)
        self.animMultiplier = 0.4
        self.setPlayRate(self.animMultiplier, 'walk') 
        self.reparentTo(render)
