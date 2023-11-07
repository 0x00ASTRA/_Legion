from classes.hardware.hardware_component import HardwareComponent

class CPU(HardwareComponent):
    def __init__(self, brand: str, model: str, speed: int):
        super().__init__('CPU')
        self.brand = brand
        self.model = model
        self.speed = speed

    def overclock(self, amount: int):
        self.speed += amount

class GPU(HardwareComponent):
    def __init__(self, brand: str, model: str, memory: int, speed: int):
        super().__init__('GPU')
        self.brand = brand
        self.model = model
        self.memory = memory
        self.speed = speed

class RAM(HardwareComponent):
    def __init__(self, size: int):
        super().__init__('RAM')
        self.size = size

class Storage(HardwareComponent):
    def __init__(self, type: enumerate, size: int, speed: int):
        super().__init__('Storage')
        self.type = type
        self.size = size
        self.speed = speed
