from Spells.Spell import Spell

from Spells.NormalAttack import NormalAttack
from Spells.HeavyAttack import HeavyAttack
from Spells.SpellAttack import SpellAttack
from Spells.MakeDamageShield import MakeDamageShield
from Spells.DarkConversion import DarkConversion
from Spells.HauntingCurse import HauntingCurse
from Spells.Surge import Surge
from Spells.Idle import Idle
from Spells.ElementalDrain import ElementalDrain
from Spells.Hurricane import Hurricane


skillSetUp1: [Spell] = [

    MakeDamageShield(8),

    DarkConversion(7),

    Surge(6),

    ElementalDrain(5),

    Hurricane(4),

    HauntingCurse(3),

    HeavyAttack(2),

    # NormalAttack(3),

    SpellAttack(1),

    Idle(0, SpellAttack().spellBar)

]


