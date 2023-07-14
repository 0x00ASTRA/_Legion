class CPU:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

class GPU:
    def __init__(self, brand, model, memory):
        self.brand = brand
        self.model = model
        self.memory = memory

class RAM:
    def __init__(self, size):
        self.size = size

class Storage:
    def __init__(self, type, size):
        self.type = type
        self.size = size
