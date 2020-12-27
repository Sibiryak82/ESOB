from Spells.Spell import Spell, CurrentStates
from BasicControls import BasicControls
from SearchForEnemy.MoveToEnemy import MoveToEnemy

import time


class WeavingAttack(Spell):
    spellName = "WeavingAttack"

    spellBar = 0
    spellSlot = 0

    priority = 3

    count = 0

    def __init__(self, priority=3):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if states.isTargetingEnemy:
            return True
        else:
            return False

    def use(self):
        BasicControls.getInstance().swapToSpellBar1()
        MoveToEnemy.getInstance().moveToEnemyShort()

        BasicControls.getInstance().normalAttack()

        if self.currentStates.haveEnoughMagicka:
            BasicControls.getInstance().spell1()
            time.sleep(0.9)


if __name__ == "__main__":
    spell: Spell = WeavingAttack()
    state: CurrentStates = CurrentStates()

    state.isTargetingEnemy = False

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()
    state2.isTargetingEnemy = True
    state2.haveEnoughMagicka = False
    print(spell.shouldUseThisSpell(state2))

    spell.use()




