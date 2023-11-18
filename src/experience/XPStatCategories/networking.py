from src.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Networking(XPStatCategory):
   def __init__(
       self,
      fundimentals: int =0,
      security: int=0,
      architecture: int =0,
      redundancy: int =0
   ):
      self.fundimentals = fundimentals
      self.security = security
      self.architecture = architecture
      self.redundacy = redundancy