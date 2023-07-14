class Computer:
    def __init__(self, CPU, GPU, RAM, storage):
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
        self.storage = storage
        self.is_compromised = False

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
