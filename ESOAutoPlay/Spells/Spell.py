# [SpellName, SpellBar (1 | 2), spellSlot ( 1...5 ), coolDown, using condition]
from CurrentStates import CurrentStates
from BasicControls import BasicControls
import time


class Spell:
    spellName = ""
    spellBar = 1
    spellSlot = 1

    priority = 0  # bigger priority have higher priority

    currentStates: CurrentStates

    def __init__(self):
        pass

    def shouldUseThisSpell(self, states: CurrentStates) -> bool:
        return True

    def use(self):

        if self.spellName == "HeavyAttack":
            # print("HeavyAttack", self.currentStates)
            BasicControls.getInstance().heavyAttack()
            return

        if self.spellName == "NormalAttack":
            BasicControls.getInstance().normalAttack()
            return

        if self.spellBar == 1:
            if not self.currentStates.currentSkillBar:
                BasicControls.getInstance().swapToSpellBar1()
        elif self.spellBar == 2:
            if self.currentStates.currentSkillBar:
                BasicControls.getInstance().swapToSpellBar2()

        if self.spellSlot == 0:
            return
        elif self.spellSlot == 1:
            BasicControls.getInstance().spell1()
        elif self.spellSlot == 2:
            BasicControls.getInstance().spell2()
        elif self.spellSlot == 3:
            BasicControls.getInstance().spell3()
        elif self.spellSlot == 4:
            BasicControls.getInstance().spell4()
        elif self.spellSlot == 5:
            BasicControls.getInstance().spell5()

        # print(f"spell {self.spellName}, Bar {self.spellBar}, Slot {self.spellSlot}, Priority {self.priority} using")
        return
