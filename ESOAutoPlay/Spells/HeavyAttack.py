from Spells.Spell import Spell, CurrentStates
import time


class HeavyAttack(Spell):
    spellName = "HeavyAttack"

    spellBar = 0
    spellSlot = 0

    priority = 5

    def __init__(self, priority=5):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if states.isTargetingEnemy and not states.haveEnoughMagicka:
            return True
        else:
            return False



if __name__ == "__main__":
    spell: Spell = HeavyAttack()
    state: CurrentStates = CurrentStates()

    state.isTargetingEnemy = False

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()
    state2.isTargetingEnemy = True
    state2.haveEnoughMagicka = False
    print(spell.shouldUseThisSpell(state2))

    spell.use()




