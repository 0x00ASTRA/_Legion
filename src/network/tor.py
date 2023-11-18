from .network import Node, Network
import random

class TorNode(Node):
    def __init__(self):
        super().__init__()
    

class TorNetwork(Network):
    def __init__(self):
        super().__init__()

    def send_packet(self, packet, target_id):
        next_hop = random.choice(self.nodes)
        next_hop.send_packet(packet, target_id)
    
    def populate_network(self, num_nodes: int):
        for i in range(num_nodes):
            self.nodes.append(TorNode())
