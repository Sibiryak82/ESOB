from Spells.Spell import Spell
from Spells.Idle import Idle

from StaminaDragonknight.ResolvingVigor import ResolvingVigor
from StaminaDragonknight.RingOfPreservation import RingOfPreservation
from StaminaDragonknight.HardenedArmor import HardenedArmor
from StaminaDragonknight.Rally import Rally
from StaminaDragonknight.WeavingAttack import WeavingAttack
from StaminaDragonknight.MoltenArmaments import MoltenArmaments

setUp1: [Spell] = [

    ResolvingVigor(5),
    RingOfPreservation(4),
    HardenedArmor(3),
    MoltenArmaments(2),
    WeavingAttack(1),

    Idle(0)
]