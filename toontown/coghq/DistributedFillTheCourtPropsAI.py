#create a class that inherits from DistributedLevelAI

from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedLevelAI, LevelSpec
import FillTheCourtSpec
from direct.distributed import DistributedObjectAI

class DistributedFillTheCourtPropsAI(DistributedLevelAI.DistributedLevelAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFillTheCourtPropsAI')
    
    def __init__(self, air, zoneId, entranceId=0, avIds=[1, 2]):
        DistributedLevelAI.DistributedLevelAI.__init__(self, air, zoneId, entranceId, avIds)
        self.zoneId = zoneId
        self.entranceId = 0
        self.air = air
        self.levelSpec = LevelSpec.LevelSpec(FillTheCourtSpec)
        self.zoneIds = [0, 1, 2, 3]
    
    def generate(self, levelSpec = None):
        self.notify.debug('generate')
        DistributedObjectAI.DistributedObjectAI.generate(self)
        if levelSpec == None:
            levelSpec = self.levelSpec
        self.initializeLevel(levelSpec)
        if __dev__:
            pass
        return