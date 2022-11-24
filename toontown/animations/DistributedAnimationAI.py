#make a class that inherits from DistributedObjectAI called DistributedAnimationAI

from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from panda3d.core import *

class DistributedAnimationAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimationAI')

    def __init__(self, air):
        self.air = air
        DistributedObjectAI.__init__(self, air)

    def generateWithRequired(self, zoneId):
        DistributedObjectAI.generateWithRequired(self, zoneId)
    
    def startAnimation(self):
        self.sendUpdate('startAnimation')