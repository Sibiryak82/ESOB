from Spells.Spell import Spell, CurrentStates
import time


class HardenedArmor(Spell):
    spellName = "HardenedArmor"

    spellBar = 2
    spellSlot = 3

    priority = 7

    nextTimeUseIt = 0
    duration = 20

    def __init__(self, priority=7):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self.nextTimeUseIt < time.time() and states.haveEnoughStamina:
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        super().use()


if __name__ == "__main__":
    spell: Spell = HardenedArmor()
    state: CurrentStates = CurrentStates()

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.haveEnoughMagicka = False

    print(spell.shouldUseThisSpell(state2))

    spell.use()

    print(spell.shouldUseThisSpell(state))



