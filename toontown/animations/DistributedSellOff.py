#make a class that inherits from DistributedAnimation called DistributedSellOff

import DistributedAnimation
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import *
from toontown.avatar import ToontownAvatarUtils
from panda3d.core import *
from libotp import *
from otp.avatar.Avatar import Avatar

class DistributedSellOff(DistributedAnimation.DistributedAnimation):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSellOff')

    def __init__(self, cr):
        self.cr = cr
        DistributedAnimation.DistributedAnimation.__init__(self, cr)
        self.animationSequence = Sequence()
        
        self.Fred = ToontownAvatarUtils.createCog('cc', name="Fred", dept="Sellbot", level=8, coll=False)
        self.Fred.setPos(-16.807, -180, -19.594)
        self.Fred.setH(245)
        self.Fred.addActive()
        
        self.Handy = ToontownAvatarUtils.createCog('gh', name="Handy", dept="Sellbot", level=12, coll=False)
        self.Handy.setPos(-9, -188.718, -19.594)
        self.Handy.setH(300)
        self.Handy.addActive()
        
        self.cameraPos1 = Point3(12, -180, 25)
        self.cameraPos2 = Point3(12, -180, -10)
        
        self.hpr1 = Point3(37, 0, 0)
        self.hpr2 = Point3(-140, 0, 0)
        

    def startAnimation(self):
        self.notify.debug('startAnimation')
        self.disableAvatarSeq = Sequence(Func(base.localAvatar.disableAvatarControls),
                                         Func(NodePath(base.localAvatar.laffMeter).hide),
                                         Func(base.localAvatar.obscureFriendsListButton, 1),
                                         Func(base.localAvatar.hideClarabelleGui),
                                         Func(base.localAvatar.invPage.ignoreOnscreenHooks),
                                         Func(base.localAvatar.questPage.ignoreOnscreenHooks),
                                         Func(NodePath(base.marginManager).hide),
                                         Func(base.localAvatar.stopUpdateSmartCamera),
                                         Func(base.localAvatar.shutdownSmartCamera))
        base.camera.reparentTo(render)
        base.camera.setPos(self.cameraPos1)
        base.camera.setH(460)
        
        self.fredHprInterval = Sequence(Func(self.Fred.loop, 'walk'),
                                        LerpHprInterval(self.Fred, duration=4, hpr=self.hpr2),
                                        Func(self.Fred.loop, 'neutral'))
        
        self.handyHprInterval = Sequence(Func(self.Handy.loop, 'walk'),
                                         LerpHprInterval(self.Handy, duration=4, hpr=self.hpr1),
                                         Func(self.Handy.loop, 'neutral'))
        
        self.irisInSeq = Sequence(Func(base.transitions.irisIn, 2.5))
        
        self.lerpCamera = LerpPosInterval(base.camera, 6, self.cameraPos2, blendType='easeInOut')
        
        self.camIrisSeq = Parallel(self.disableAvatarSeq, self.irisInSeq, self.lerpCamera)
        
        self.animationSequence.append(self.camIrisSeq)
        
        self.fredAndHandyWalk1 = Parallel(self.fredHprInterval, self.handyHprInterval)
        
        self.animationSequence.append(self.fredAndHandyWalk1)
        
        self.fredTalk = Sequence(self.getChatSequence(self.Fred, "I've broken my legs all winter, just to get a extra 3 levels...", preClear=True),
                                 self.getChatSequence(self.Fred, "It's nothing new when they gave it to every, single, SELLBOT!", preClear=True),
                                 self.getChatSequence(self.Handy, "Hey, don't worry. I'm sure if you do your job you get to my level some day!", preClear=True),
                                 self.getChatSequence(self.Fred, "I would. if doing so would'nt get me destroyed by a Birthday Cake...", preClear=True))
        
        self.animationSequence.append(self.fredTalk)
        
        self.animationSequence.start()
        
    def getChatSequence(self, obj, chat=None, chatType=0, wait=5.0, chatFlags=CFSpeech | CFTimeout, dialogue=None, interrupt=1, chatPage=0, preClear=False, postClear=False, hiddenNametag=False):
        seq = Sequence()
        if chat is not None:
            chat = chat.strip()
        hasChat = chat is not None and chat != ''
        if all(x is False for x in (hasChat, preClear, postClear)):
            preClear = True
        hiddenNametag = hiddenNametag if not isinstance(obj, Avatar) else False
        if preClear:
            seq.append(Func(obj.clearChat))
        if hasChat:
            if isinstance(obj, Avatar):
                if chatType == 0 and not hasattr(obj, 'doId'):
                    chatType = 1
                if chatType == 0:
                    seq.append(Func(obj.displayTalk, chat))
                elif chatType == 1:
                    seq.append(Func(obj.setChatAbsolute, chat, chatFlags, dialogue, interrupt))
                else:
                    self.notify.warning('ChatType not defined.')
            elif hiddenNametag:
                seq.append(obj.show)
            else:
                seq.append(Func(obj.setChat, chat, chatFlags, chatPage))

            if wait > -0.0:
                seq.append(Wait(wait))
                if postClear:
                    seq.append(Func(obj.clearChat))
                    if hiddenNametag:
                        seq.append(obj.hide)
        elif wait > -0.0:
            seq.append(Wait(wait))
            if postClear and not preClear:
                seq.append(Func(obj.clearChat))
                if hiddenNametag:
                    seq.append(obj.hide)
        elif wait <= -0.0 and not preClear and postClear:
            seq.append(Func(obj.clearChat))
            if hiddenNametag:
                seq.append(obj.hide)
        return seq
    
    def stopAnimation(self):
        self.notify.debug('stopAnimation')