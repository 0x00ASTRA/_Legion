from classes.experience.XPCategories.xp_cateory import XPCategory
from classes.experience.XPStatCategories.tactics import Tactics
from classes.experience.XPStatCategories.combat import Combat
from classes.experience.XPStatCategories.survival import Survival

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
