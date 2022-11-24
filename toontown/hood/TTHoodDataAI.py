from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.safezone import DistributedTrolleyAI
from toontown.safezone import TTTreasurePlannerAI, DistributedIntelTreasureAI
from toontown.classicchars import DistributedMickeyAI
from toontown.safezone import ButterflyGlobals
from direct.task import Task
from toontown.suit import DistributedBossbotHQGoonAI

class TTHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTHoodDataAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.ToontownCentral
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        
        
        #generate Resistance Pipe
        self.addDistObj(trolley)
        self.trolley = trolley
        self.treasurePlanner = TTTreasurePlannerAI.TTTreasurePlannerAI(self.zoneId)
        self.intelTresure = DistributedIntelTreasureAI.DistributedIntelTreasureAI(self.air, self.treasurePlanner, 106, 1.0, 4.575)
        self.intelTresure.generateWithRequired(self.zoneId)
        self.treasurePlanner.start()
        self.classicChar = DistributedMickeyAI.DistributedMickeyAI(self.air)
        self.classicChar.generateWithRequired(self.zoneId)
        self.classicChar.start()
        self.addDistObj(self.classicChar)
        self.createButterflies(ButterflyGlobals.TTC)
        if simbase.blinkTrolley:
            taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        messenger.send('TTHoodSpawned', [self])

    def shutdown(self):
        HoodDataAI.HoodDataAI.shutdown(self)
        messenger.send('TTHoodDestroyed', [self])

    def _deleteTrolley(self, task):
        self.trolley.requestDelete()
        taskMgr.doMethodLater(0.5, self._createTrolley, 'createTrolley')
        return Task.done

    def _createTrolley(self, task):
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.trolley = trolley
        taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        return Task.done
