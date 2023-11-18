from src.experience.XPCategories.xp_cateory import XPCategory
from src.experience.XPStatCategories.hacking import Hacking
from src.experience.XPStatCategories.hardware import Hardware
from src.experience.XPStatCategories.programming import Programming
from src.experience.XPStatCategories.networking import Networking

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