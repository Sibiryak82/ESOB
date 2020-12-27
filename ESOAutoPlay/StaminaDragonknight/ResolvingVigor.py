from Spells.Spell import Spell, CurrentStates
import time


class ResolvingVigor(Spell):
    spellName = "ResolvingVigor"

    spellBar = 1
    spellSlot = 5

    priority = 7

    def __init__(self, priority=7):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if not self.currentStates.haveEnoughHealth:
            return True
        else:
            return False



if __name__ == "__main__":
    spell: Spell = ResolvingVigor()
    state: CurrentStates = CurrentStates()

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.haveEnoughMagicka = False

    print(spell.shouldUseThisSpell(state2))

    spell.use()

    print(spell.shouldUseThisSpell(state))



