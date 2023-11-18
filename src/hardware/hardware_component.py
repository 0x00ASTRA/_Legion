import json

class HardwareComponent:
    def __init__(self, specs: {}):
        self.specs = json.dumps(specs) # json string