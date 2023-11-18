from src.experience.XPCategories.xp_cateory import XPCategory
from src.experience.XPStatCategories.tactics import Tactics
from src.experience.XPStatCategories.combat import Combat
from src.experience.XPStatCategories.survival import Survival

class Tactical(XPCategory):
    def __init__(
        self,
        tactics: Tactics,
        combat: Combat,
        survival: Survival,
    ):
        self.tactics = tactics
        self.combat = combat
        self.survival = survival
