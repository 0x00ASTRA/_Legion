from typing import Dict
from hashlib import sha256
import rsa
import copy

class Packet:
    def __init__(self, data: Dict):
        req_keys = ["source", "destination", "protocol", "data", "hash", "signature"]

        for key in req_keys:
            assert key in data, f"The required key '{key}' is missing from the data constructor | GameObject: Packet"

        # Create a copy of the data and remove the hash for integrity verification
        hash_data = copy.deepcopy(data)
        hash_value = hash_data.pop("hash")

        assert sha256(str(hash_data).encode()).hexdigest() == hash_value, \
            f"The hash of the packet data does not match the provided hash | GameObject: Packet"

        self.data = data

    def view(self) -> str:
        return str(self.data)
