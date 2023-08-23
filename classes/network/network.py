import random
import uuid
import logging

class Router:
    def __init__(self):
        self.id = uuid.uuid4()
        self.online = True
        self.compromised = False
        self.reputation = 100  # Nodes start with a reputation of 100

    def go_offline(self):
        self.online = False
        self.reputation -= 10  # Going offline reduces the node's reputation

    def go_online(self):
        self.online = True

    def compromise(self):
        self.compromised = True
        self.reputation -= 50  # Getting compromised significantly reduces the node's reputation

    def receive_packet(self, packet):
        # Add logic here to handle received packet
        logging.info(f"Node {self.id} received packet {packet}")
        return True

class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def send_packet(self, packet, source_id, target_id):
        # Only online nodes can relay packets
        online_nodes = [node for node in self.nodes if node.online]
        if not online_nodes:
            raise Exception("No online nodes available to send packet")
        # The packet bounces between a random number of online nodes before reaching its destination
        num_bounces = random.randint(1, len(online_nodes))
        random.shuffle(online_nodes)
        for _ in range(num_bounces):
            node = online_nodes.pop()
            logging.info(f"Packet {packet} bounced to node {node.id}")
        return target_id.receive_packet(packet)