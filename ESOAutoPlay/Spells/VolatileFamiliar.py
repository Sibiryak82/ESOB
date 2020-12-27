from Spells.Spell import Spell, CurrentStates
import time


class VolatileFamiliar(Spell):
    spellName = "HauntingCurse"

    spellBar = 1
    spellSlot = 2

    priority = 8

    nextTimeUseIt = 0
    duration = 11

    def __init__(self, priority=8):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self.nextTimeUseIt < time.time() and states.haveEnoughMagicka and states.isTargetingEnemy:
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        super().use()


if __name__ == "__main__":
    spell: Spell = VolatileFamiliar()
    state: CurrentStates = CurrentStates()

    state.isTargetingEnemy = True

    print(spell.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.isTargetingEnemy = False
    state2.haveEnoughMagicka = False

    print(spell.shouldUseThisSpell(state2))

    spell.use()

    print(spell.shouldUseThisSpell(state))



