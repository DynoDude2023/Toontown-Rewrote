import math

from toontown.battle.SuitBattleGlobals import *
from toontown.battle.calc.BattleCalculatorGlobals import APPLY_HEALTH_ADJUSTMENTS
from toontown.battle.calc.SuitCalculatorAI import SuitCalculatorAI


class SuitSpecialCalculatorAI(SuitCalculatorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('V2SuitCalculatorAI')

    def __init__(self, battle, suit, healCalculator):
        SuitCalculatorAI.__init__(self, battle, suit, healCalculator)
        self.suit = suit
        
    def getDefense(self):
        return self.suit.getActualLevel() * 1.5
    
    def getNewCombo(self, dmg):
        combo = dmg * 0.50
        return combo - self.suit.getActualLevel() * 1.5
    
    def hitSuit(self, attack, damage):
        markedStatus = self.suit.getStatus(MARKED_STATUS)
        
        
        if not self.suit.getSkelecog():
            damage -= self.getDefense()

            attack[TOON_KBBONUS_COL][self.battle.activeSuits.index(self.suit)] = damage
        
        attack[TOON_HP_COL][self.battle.activeSuits.index(self.suit)] = damage
        
        self.suit.setHP(self.suit.getHP() - damage)
        messenger.send('suit-was-hit', [attack, damage])
    
    