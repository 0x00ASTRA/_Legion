from src.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Hacking(XPStatCategory):
   def __init__(
       self,
       fundimentals,
       recon,
       attacks,
       exploitation,
       post_expoitation,
       stealth
   ):
       self.fundimentals = fundmentals
       self.recon = recon
       self.attacks = attacks
       self.exploitation = exploitation
       self.post_exploitation = post_exploitation
       self.stealth = stealth