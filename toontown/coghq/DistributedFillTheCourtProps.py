#make a class that inherits from DistributedLevel called DistributedFillTheCourtProps

from direct.directnotify import DirectNotifyGlobal
from otp.level import DistributedLevel, LevelSpec
from direct.showbase.PythonUtil import *
import FillTheCourtSpec
from otp.level import Level, LevelConstants, LevelUtil
from otp.otpbase import OTPGlobals


class DistributedFillTheCourtProps(DistributedLevel.DistributedLevel):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFillTheCourtProps')
    doId = 1

    def __init__(self, cr):
        DistributedLevel.DistributedLevel.__init__(self, cr)
        self.cr = cr
        self.levelSpec = LevelSpec.LevelSpec(FillTheCourtSpec)
        self.zoneNums = [0, 1, 2, 3]
        self.zoneNumDict = {}
        self.entranceId = 0
        self.levelZone = 0
        self.zoneNum2zoneId = {0: 11000, 1: 11000, 2: 11000, 3: 11000}
        self.curVisibleZoneNums = list2dict(self.zoneNums)
        self.initializeLevel(self.levelSpec)

    
    def hideZone(self, zoneNum):
        pass
    
    def onEntityTypePostCreate(self, entType):
        pass
    
    def getZoneNode(self, zoneEntId):
        pass
    
    def requestReparent(self, entity, parentId, wrt = False):
        parent = self.getEntity(parentId)
        if parent is not None:
            if wrt:
                entity.wrtReparentTo(parent.getNodePath())
            else:
                entity.reparentTo(parent.getNodePath())
        else:
            DistributedLevel.notify.debug('entity %s requesting reparent to %s, not yet created' % (entity, parentId))
            entity.reparentTo(hidden)
            if parentId not in self.parent2pendingChildren:
                self.parent2pendingChildren[parentId] = []

                def doReparent(parentId = parentId, self = self, wrt = wrt):
                    parent = self.getEntity(parentId)
                    for child in self.parent2pendingChildren[parentId]:
                        DistributedLevel.notify.debug('performing pending reparent of %s to %s' % (child, parent))
                        if wrt:
                            child.wrtReparentTo(parent.getNodePath())
                        else:
                            child.reparentTo(parent.getNodePath())

                    del self.parent2pendingChildren[parentId]
                    self.ignore(self.getEntityCreateEvent(parentId))

                self.accept(self.getEntityCreateEvent(parentId), doReparent)
            self.parent2pendingChildren[parentId].append(entity)
        return
    
    def initVisibility(self):
        self.curZoneNum = None
        self.visChangedThisFrame = 0
        self.fForceSetZoneThisFrame = 0

        def handleCameraRayFloorCollision(collEntry, self = self):
            name = collEntry.getIntoNode().getName()
            self.notify.debug('camera floor ray collided with: %s' % name)
            prefixLen = len(DistributedLevel.FloorCollPrefix)
            if name[:prefixLen] == DistributedLevel.FloorCollPrefix:
                try:
                    zoneNum = int(name[prefixLen:])
                except:
                    DistributedLevel.notify.warning('Invalid zone floor collision node: %s' % name)
                else:
                    self.camEnterZone(zoneNum)
    
    def setVisibility(self, vizList):
        uberZone = self.getZoneId(LevelConstants.UberZoneEntId)
        visibleZoneIds = [OTPGlobals.UberZone, self.levelZone, uberZone]
        for vz in vizList:
            if vz is not LevelConstants.UberZoneEntId:
                visibleZoneIds.append(self.getZoneId(vz))

    def resetVisibility(self):
        pass