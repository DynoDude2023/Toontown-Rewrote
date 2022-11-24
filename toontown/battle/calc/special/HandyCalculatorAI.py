import math

from toontown.battle.SuitBattleGlobals import *
from toontown.battle.calc.BattleCalculatorGlobals import APPLY_HEALTH_ADJUSTMENTS
from toontown.battle.calc.SuitCalculatorAI import SuitCalculatorAI


class SuitSpecialCalculatorAI(SuitCalculatorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('HandyCalculatorAI')

    def __init__(self, battle, suit, healCalculator):
        SuitCalculatorAI.__init__(self, battle, suit, healCalculator)
        self.attackPower = 1.0
        self.accept('suit-killed', self.__compensate)

    def __compensate(self, suit):
        movie = [self.suit.doId, 4, 0, [32, 32, 32, 32], 0, 0, 0]
        self.battle.suitAttacks.append(movie)
        self.attackPower *= 1.15

    def __applySuitAttackDamages(self, attackIndex):
        attack = self.battle.suitAttacks[attackIndex]
        attack = math.ceil(attack * self.attackPower)
        if APPLY_HEALTH_ADJUSTMENTS:
            for toon in self.battle.activeToons:
                self.healCalculator.hurtToon(attack, toon)
