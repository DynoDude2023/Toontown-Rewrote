#make a class that inherits from DistributedObject called DistributedAnimation

from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import *
from panda3d.core import *

class DistributedAnimation(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimation')

    def __init__(self, cr):
        self.cr = cr
        DistributedObject.__init__(self, cr)
        self.animationSequence = Sequence()
    
    def startAnimation(self):
        pass