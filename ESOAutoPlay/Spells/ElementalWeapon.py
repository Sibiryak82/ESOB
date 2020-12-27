from Spells.Spell import Spell, CurrentStates
from pynput.keyboard import Key
import pynput
import time


class ElementalWeapon(Spell):
    spellName = "SpellAttack"

    spellBar = 1
    spellSlot = 1

    priority = 5
    keyboard = None

    def __init__(self, priority=5):
        Spell.__init__(self)

        self.priority = priority
        self.keyboard = pynput.keyboard.Controller()

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if states.currentSkillBar:
            self.spellBar = 0
        else:
            self.spellBar = 1

        if states.isTargetingEnemy and states.haveEnoughMagicka:
            return True
        else:
            return False

    def click(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)
        return

    def use(self):
        print("ElementalWeapon")
        self.click(Key.f15)
        time.sleep(0.38)
        self.click("`")
        time.sleep(0.38)
        self.click(Key.f14)
        time.sleep(0.38 - 0.17)




if __name__ == "__main__":
    attack: Spell = ElementalWeapon()
    state: CurrentStates = CurrentStates()

    print(attack.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.haveDamageShield = True
    state2.isTargetingEnemy = True
    state2.haveEnoughHealth = True
    state2.haveEnoughMagicka = True

    print(attack.shouldUseThisSpell(state2))

    attack.use()



