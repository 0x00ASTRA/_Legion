class Attack:
    def __init__(self, name):
        self.name = name

class Virus(Attack):
    def __init__(self):
        super().__init__("Virus")

class Ransomware(Attack):
    def __init__(self):
        super().__init__("Ransomware")

class Worm(Attack):
    def __init__(self):
        super().__init__("Worm")

class Phishing(Attack):
    def __init__(self):
        super().__init__("Phishing")

class Exploit(Attack):
    def __init__(self):
        super().__init__("Exploit")
