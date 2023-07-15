class LevelingSystem:
    def __init__(self, xp_to_level_up: int):
        self.xp = 0
        self.level = 1
        self.xp_to_level_up = xp_to_level_up

    def increment_xp(self, xp: int):
        self.xp += xp
        while self.xp >= self.xp_to_level_up:
            self.level_up()
            self.xp -= self.xp_to_level_up

    def level_up(self):
        self.level += 1

    def to_json(self):
        return {"xp": self.xp, "level": self.level, "xp_to_level_up": self.xp_to_level_up}