import classes.utils as utils
from classes.filesystem import Filesystem
class Computer:
    def __init__(self, CPU, GPU, RAM, storage):
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
        self.storage = storage
        self.is_compromised = False
        self.serial_id = utils.generate_serial_id()
        self.filesystem = Filesystem('/')

    def list_files(self) -> str:
        return str(self.filesystem.contains)