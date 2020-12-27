from Spells.Spell import Spell, CurrentStates
from BasicControls import BasicControls
from SearchForEnemy.MoveToEnemy import MoveToEnemy


class SpellAttack(Spell):
    spellName = "SpellAttack"

    spellBar = 2
    spellSlot = 1

    priority = 5

    def __init__(self, priority=5):
        Spell.__init__(self)

        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if states.isTargetingEnemy and states.haveEnoughMagicka:
            return True
        else:
            return False

    def use(self):
        from _Configuration import useAutoWalk
        if useAutoWalk:
            MoveToEnemy.getInstance().moveToEnemyLong()
        BasicControls.getInstance().normalAttack()

        if self.currentStates.sp1:
            self.spellSlot = 3
        else:
            self.spellSlot = 1
        super().use()


if __name__ == "__main__":
    attack: Spell = SpellAttack()
    state: CurrentStates = CurrentStates()

    print(attack.shouldUseThisSpell(state))

    state2: CurrentStates = CurrentStates()

    state2.haveDamageShield = True
    state2.isTargetingEnemy = True
    state2.haveEnoughHealth = True
    state2.haveEnoughMagicka = True

    print(attack.shouldUseThisSpell(state2))

    attack.use()



