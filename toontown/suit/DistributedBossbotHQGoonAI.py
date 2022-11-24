import DistributedGoonAI
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
from GoonGlobals import *
import GoonPathData
import random
from panda3d.core import *
from otp.ai.AIBaseGlobal import *
from GoonGlobals import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
import GoonPathData
from direct.distributed import ClockDelta
import random
from direct.task import Task

class DistributedBossbotHQGoonAI(DistributedGoonAI.DistributedGoonAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBossbotHQGoonAI')
    STUN_TIME = 4
    
    def __init__(self, air, entId):
        self.hFov = 30
        self.entId = entId
        self.attackRadius = 10
        self.strength = 40
        self.velocity = 5
        self.scale = 2.5
        DistributedGoonAI.DistributedGoonAI.__init__(self, air, entId)

        self.goonType = 'sg'
        return
    
    def generate(self):
        self.startGoon()
    
    def setEntId(self, entId):
        self.entId = entId
    
    def d_setEntId(self, entId):
        self.sendUpdate('setEntId', [entId])
    
    def b_setEntId(self, entId):
        self.d_setEntId(entId)
        self.setEntId(entId)
    
    def getEntId(self):
        return self.entId
    
    def requestBattle(self, time):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)
        if avatar:
            avatar.takeDamage(40)
        DistributedGoonAI.DistributedGoonAI.requestBattle(self, 4)
    
    def setParameterize(self, x, y, z, pathIndex):
        pass
    
