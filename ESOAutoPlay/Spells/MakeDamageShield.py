from Spells.Spell import Spell, CurrentStates


class MakeDamageShield(Spell):
    spellName = "MakeDamageShield"

    spellBar = 2
    spellSlot = 5

    priority = 11

    def __init__(self, priority=11):
        Spell.__init__(self)

        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if not states.haveDamageShield:
            return True
        else:
            return False


if __name__ == "__main__":
    attack: Spell = MakeDamageShield(10)
    state: CurrentStates = CurrentStates()

    print(attack.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.haveDamageShield = True

    print(attack.shouldUseThisSpell(state2))

    attack.use()



