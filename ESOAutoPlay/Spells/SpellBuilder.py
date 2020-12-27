from Spells.Spell import Spell, CurrentStates
import time


class SpellBuilder(Spell):
    spellName = "SpellBuilder"

    spellBar = 0
    spellSlot = 0

    priority = 0

    _nextTimeUseIt = 0
    duration = 20

    def __init__(self, bar, slot, duration, priority):
        Spell.__init__(self)
        self.spellBar = bar
        self.spellSlot = slot
        self.duration = duration

        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self._nextTimeUseIt < time.time():
            return True
        else:
            return False

    def use(self):
        self._nextTimeUseIt = time.time() + self.duration
        # print(self.spellName, self.currentStates)
        super().use()



