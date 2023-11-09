from classes.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Survival(XPStatCategory):
  def __init__(
      self,
      wilderness_skills: int =0,
      first_aid: int =0,
      resourcefulness: int =0,
      navigation: in =0
  ):
      self.wilderness_skills = wilderness_skills
      self.first_aid = first_aid
      self.resourcefulness = resourcefulness
      self.navigation = navigation