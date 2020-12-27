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

    lastTimeUseVenomousClaw = 0.0
    lastTimeUseNoxiousBreath = 0.0

    def use(self):
        BasicControls.getInstance().swapToSpellBar1()
        MoveToEnemy.getInstance().moveToEnemyShort()
        BasicControls.getInstance().heavyAttack(1.25)
        # if self.count == 0:
        #     BasicControls.getInstance().spell2()  # brawler
        # elif self.count == 1:
        #     BasicControls.getInstance().spell3()  # venomous claw
        # elif self.count == 2:
        #     BasicControls.getInstance().spell4()  # noxious breath
        if self.lastTimeUseVenomousClaw + 13 < time.time():
            BasicControls.getInstance().spell3()  # venomous claw
            self.lastTimeUseVenomousClaw = time.time()
        elif self.lastTimeUseNoxiousBreath + 13 < time.time():
            BasicControls.getInstance().spell4()  # noxious breath
            self.lastTimeUseNoxiousBreath = time.time()

        else:
            BasicControls.getInstance().spell2()  # brawler




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




