from Spells import SkillSetUps
from StaminaDragonknight import SkillSetUps as SD
from MagickaTemplar import _SkillSetUp as MagT1
from Spells.SpellBuilder import SpellBuilder
from Spells.Idle import Idle

useAutoWalk = True
useFollowTarget = True
useEnemyFinder = False

# usingSkillSetUp = SkillSetUps.skillSetUp1
# usingSkillSetUp = SD.setUp1
# usingSkillSetUp = MagT1.s1


usingSkillSetUp = [  # MagT Heal
    SpellBuilder(2, 1, 10, 9),
    SpellBuilder(2, 2, 10, 9),
    SpellBuilder(2, 2, 10, 9),
    SpellBuilder(2, 3, 24, 9),
    SpellBuilder(2, 4, 20, 9),
    Idle(2)


]


# usingSkillSetUp = [  # SS
#     SpellBuilder(2, 1, 14, 9),
#
#     SpellBuilder(2, 4, 33, 9),
#     SpellBuilder(2, 5, 15, 9),
#     Idle(2)
#
#
# ]