from direct.actor import Actor
from otp.avatar import Avatar
from direct.interval.IntervalGlobal import *

#make a class called Boiler based on Avatar

boilerAnims = ['idle', 'intro']

class Boiler(Avatar.Avatar):
    
    def __init__(self):
        Avatar.Avatar.__init__(self)
        self.makeActor()
        self.makeAnimations()
    
    def makeActor(self):
        #load the boiler model
        self.boilerBase = Actor.Actor('phase_5/models/char/ttr_r_chr_cbg_boss')
        
        
    def makeAnimations(self):
        animBase = 'phase_5/models/char/ttr_a_chr_cbg_boss_'
        
        for anim in boilerAnims:
            self.boilerBase.loadAnims({anim:animBase + anim + '.bam'})
        
        self.boilerBase.setBlend(frameBlend = True)
        self.boilerBase.loop('idle')