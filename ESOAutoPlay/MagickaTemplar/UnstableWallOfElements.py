from Spells.Spell import Spell, CurrentStates
import time


class UnstableWallOfElements(Spell):
    spellName = "UnstableWallOfElements"

    spellBar = 1
    spellSlot = 2

    priority = 7

    nextTimeUseIt = 0
    duration = 10

    def __init__(self, priority=7):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self.nextTimeUseIt < time.time() and states.haveEnoughMagicka and states.isTargetingEnemy:
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        super().use()