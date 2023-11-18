from src.experience.XPStatCategories.xp_stat_category import XPStatCategory

class Programming(XPStatCategory):
    def __init__(
        self,
        fundamentals: int = 0,
        paradigms: int = 0,
        logic: int = 0,
        control_flow: int = 0,
        languages: int = 0,
        language_mastery: int = 0,
        data_analysis: int = 0,
    ):
        self.fundamentals = fundamentals
        self.paradigms = paradigms
        self.logic = logic
        self.control_flow = control_flow
        self.languages = languages
        self.language_mastery = language_mastery
        self.data_analysis = data_analysis