from Spells.Spell import Spell, CurrentStates
import time
from BasicControls import BasicControls


class NormalAttack(Spell):
    spellName = "NormalAttack"

    spellBar = 0
    spellSlot = 0

    priority = 6

    nextTimeUseIt = 0
    duration = 9

    def __init__(self, priority=6):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self.nextTimeUseIt < time.time() and states.isTargetingEnemy:
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        BasicControls.getInstance().normalAttack()


if __name__ == "__main__":
    spell: Spell = NormalAttack()
    state: CurrentStates = CurrentStates()
    state.isTargetingEnemy = False
    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()
    state2.isTargetingEnemy = True
    print(spell.shouldUseThisSpell(state2))

    spell.use()

    print(spell.shouldUseThisSpell(state))



