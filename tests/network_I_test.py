
import sys
import os

# Get the absolute path of the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the root directory to the Python path
sys.path.append(root_path)

from classes.hardware.network_interface import NetworkInterface
import json

manufacturer = "My Company"
partname = "Net Card Alpha"
part_no = 532001
tx_speed = 500
rx_speed = 500
specs = {
    "specs": {
        "manufacturer": manufacturer,
        "partName": partname,
        "partNumber": part_no,
        "txSpeed": tx_speed,
        "rxSpeed": rx_speed
    }
}
net_i = NetworkInterface(specs)

print(net_i.__dict__)