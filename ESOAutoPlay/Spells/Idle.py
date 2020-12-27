from Spells.Spell import Spell, CurrentStates
import time


class Idle(Spell):
    spellName = "Idle"

    spellBar = 0
    spellSlot = 0

    priority = 0

    def __init__(self, priority=0, bar=0):
        Spell.__init__(self)
        self.priority = priority
        self.spellBar = bar

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        return True



if __name__ == "__main__":
    spell: Spell = Idle()
    state: CurrentStates = CurrentStates()

    state.isTargetingEnemy = False
    state.haveEnoughMagicka = False


    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()
    state2.isTargetingEnemy = False
    print(spell.shouldUseThisSpell(state2))

    spell.use()




