import os
import sys
import rsa
from hashlib import sha256

# Define the project's root directory path
current_file_path = os.path.abspath(__file__)
root_path = os.path.dirname(os.path.dirname(current_file_path))

# Add the root directory to the Python path
sys.path.append(root_path)

from src.network.packet import Packet

# Sample data
data = {
    "source": "src",
    "destination": "dest",
    "protocol": "UDP",
    "data": {
        "x": "10101010",
        "y": ["1fr4", "gsd44", "jj3342"],
        "z": 12144421235
    },
}

# Function to generate RSA keys
def generate_rsa_keys():
    pub_key, priv_key = rsa.newkeys(2048)  # Generating 2048-bit RSA keys
    return pub_key, priv_key

# Generate new RSA keys
pub_key, priv_key = generate_rsa_keys()

# Convert the data to bytes before signing
data_bytes = str(data).encode()

# Sign the message with the private key using SHA256 hash method
signature = rsa.sign(message=data_bytes, priv_key=priv_key, hash_method='SHA-256')

# Convert the signature to a hexadecimal string
signature_str = signature.hex()

# Update data with the signature
data["signature"] = signature_str

# Generate the packet hash
p_hash = sha256(str(data).encode()).hexdigest()
data["hash"] = p_hash

print(data)

p1 = Packet(data=data)

