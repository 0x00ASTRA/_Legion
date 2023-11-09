from classes.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Combat(XPStatCategory):
  def __init__(
      self,
      weapon_proficiency: int =0,
      cqb: int =0,
      hand2hand: int =0,
      marksmanship: int =0,
      tactical_maneuvers: int =0
  ):
      self.weapon_proficiency = weapon_proficiency
      self.cqb = cqb
      self.hand2haand = hand2hand
      self.marksmanship = marksmanship
      self.tactical_maneuvers = tactical_maneuvers
