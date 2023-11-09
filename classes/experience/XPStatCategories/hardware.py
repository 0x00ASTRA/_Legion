from classes.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Hardware(XPStatCategory):
   def __ini__(
       self,
       fundimentals: int =0,
       electrical: int =0,
       architecture: int =0,
       logic: int =0,
       efficiency: int =0
   ):
   self.fundimentals = fundimentals
   self.electrical = electrical
   self.architecture = architecture
   self.logic = logic
   self.efficiency = efficiency
