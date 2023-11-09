from classes.experience.XPCategories.xp_cateory import XPCategory
from classes.experience.XPStatCategories.hacking import Hacking
from classes.experience.XPStatCategories.hardware import Hardware
from classes.experience.XPStatCategories.programming import Programming
from classes.experience.XPStatCategories.networking import Networking

class IT(XPCategory):
    def __init__(
        self,
        hacking: Hacking,
        programming: Programming,
        networking: Networking,
        hardware: Hardware,
    ):
        self.hacking = hacking
        self.programming = programming
        self.networking= networking
        self.hardware = hardware