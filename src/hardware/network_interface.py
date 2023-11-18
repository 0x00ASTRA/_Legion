from src.hardware.hardware_component import HardwareComponent
from src.network.network import Network
from src.network.packet import Packet

class NetworkInterface(HardwareComponent):
    def __init__(self, specs: str):
        super().__init__(specs)

        # required specs keys
        req_keys = [ "manufacturer", "partName", "partNumber", "txSpeed", "rxSpeed" ]

        # Ensures the part specs follow this structure
        for key in req_keys:
            assert key in self.specs, f"The required key '{key}' is missing from specs | part: Network Interface"
  
    def transmit(packet: Packet, network: Network):
        
        pass