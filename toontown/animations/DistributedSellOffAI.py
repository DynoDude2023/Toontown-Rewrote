#make a class that inherits from DistributedAnimationAI called DistributedSellOffAI

import DistributedAnimationAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals

class DistributedSellOffAI(DistributedAnimationAI.DistributedAnimationAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSellOffAI')

    def __init__(self, air):
        DistributedAnimationAI.DistributedAnimationAI.__init__(self, air)

        
    def startAnimation(self):
        self.sendUpdate('startAnimation')
        
        