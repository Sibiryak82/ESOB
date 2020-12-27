from Spells.Spell import Spell, CurrentStates
from BasicControls import BasicControls


class HonorTheDead(Spell):
    spellName = "HonorTheDead"

    spellBar = 2
    spellSlot = 5

    priority = 5

    def __init__(self, priority=5):
        Spell.__init__(self)

        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if not states.haveEnoughHealth:
            return True
        else:
            return False


