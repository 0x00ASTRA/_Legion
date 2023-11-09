from classes.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Tactics(XPStatCategory):
  def __init__(
      self,
      strategy: int =0,
      planning: int =0,
      adaptability: int =0,
      decision_making: int =0,
      risk_assessment: int =0
  ):
      self.strategy = strategy
      self.planning = planning
      self.adaptability = adaptability
      self.decision_making = decision_making
      self.risk_assessment = risk_assessment
