from Spells.Spell import Spell, CurrentStates
import time


class DarkConversion(Spell):
    spellName = "DarkConversion"

    spellBar = 1
    spellSlot = 2

    priority = 9

    nextTimeUseIt = 0
    duration = 19

    def __init__(self, priority=9):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if not states.haveEnoughHealth:
            return True
        elif self.nextTimeUseIt < time.time() and states.haveEnoughStamina:
            return True
        elif (not states.haveEnoughMagicka) and self.nextTimeUseIt - 13 < time.time():
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        # print(self.spellName, self.currentStates)
        super().use()


if __name__ == "__main__":
    spell: Spell = DarkConversion()
    state: CurrentStates = CurrentStates()

    state.haveEnoughHealth = True

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    print(spell.shouldUseThisSpell(state2))

    spell.use()

    print(spell.shouldUseThisSpell(state2))



