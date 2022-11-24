#make a class that inherits from DistributedLawbotBoss

from direct.directnotify import DirectNotifyGlobal
import DistributedLawbotBoss
from toontown.toonbase import ToontownGlobals

class DistributedChiefJustice(DistributedLawbotBoss.DistributedLawbotBoss):
    
    def __init__(self, cr):
        DistributedLawbotBoss.DistributedLawbotBoss.__init__(self, cr)