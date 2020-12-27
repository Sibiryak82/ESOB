class TargetDirection:
    in_front = False
    behind = False
    left = False
    right = False


class CurrentStates:
    gameIsReady = False

    haveDamageShield = False
    haveEnoughHealth = True
    haveEnoughMagicka = True
    haveEnoughStamina = True

    currentSkillBar = True  # True : 1, False : 2
    isTargetingEnemy = False

    targetInShortRange = False
    targetInLongRange = False

    canUseUlt = False

    sp1 = False

    targetDirection = TargetDirection()

    def __str__(self):
        return f"haveDamageShield: {self.haveDamageShield}; haveEnoughHealth: {self.haveEnoughHealth}; " \
               f"haveEnoughMagicka: {self.haveEnoughMagicka}; haveEnoughStamina: {self.haveEnoughStamina}; " \
               f"isTargetingEnemy: {self.isTargetingEnemy}; targetInShortRange: {self.targetInShortRange}; " \
               f"targetInLongRange: {self.targetInLongRange}"


