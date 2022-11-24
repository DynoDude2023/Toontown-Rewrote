from direct.showbase.DirectObject import DirectObject
from direct.showbase.MessengerGlobal import messenger
from direct.directnotify import DirectNotifyGlobal


class CogCalcAI(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogCalcAI')

    def __init__(self, battle, suit):
        DirectObject.__init__(self)
        self.battle = battle

