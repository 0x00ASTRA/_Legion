import socket
import json
import threading
import time

class P2PNode:
    def __init__(self, node_id, port):
        self.node_id = node_id
        self.port = port
        self.peers = set()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', port))
        self.server_socket.listen(5)

    def add_peer(self, peer):
        self.peers.add(peer)

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            peer.send_transaction(transaction)

    def broadcast_block(self, block):
        for peer in self.peers:
            peer.send_block(block)

    def run_server(self):
        while True:
            client_socket, address = self.server_socket.accept()
            peer = P2PPeer(client_socket, address, self)
            self.add_peer(peer)
            threading.Thread(target=peer.receive_data).start()

class P2PPeer:
    def __init__(self, socket, address, node):
        self.socket = socket
        self.address = address
        self.node = node

    def send_transaction(self, transaction):
        data = {'type': 'transaction', 'transaction': transaction}
        self.send_data(data)

    def send_block(self, block):
        data = {'type': 'block', 'block': block}
        self.send_data(data)

    def send_data(self, data):
        serialized_data = json.dumps(data).encode('utf-8')
        self.socket.sendall(serialized_data)

    def receive_data(self):
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            self.process_data(decoded_data)

    def process_data(self, data):
        try:
            json_data = json.loads(data)
            data_type = json_data.get('type')
            if data_type == 'transaction':
                transaction = json_data.get('transaction')
                self.node.broadcast_transaction(transaction)
            elif data_type == 'block':
                block = json_data.get('block')
                self.node.broadcast_block(block)
        except json.JSONDecodeError:
            print(f"Error decoding data: {data}")

class BlockchainNode(P2PNode):
    def __init__(self, node_id, port):
        super().__init__(node_id, port)
        self.mempool = []

    def mine_block(self, miner_address):
        mined_block = {
            'transactions': self.mempool,
            'miner': miner_address,
            'timestamp': time.time(),
            # Add other block information such as previous hash, etc.
        }
        self.broadcast_block(mined_block)

# Example usage
node1 = BlockchainNode(node_id=1, port=5000)
node2 = BlockchainNode(node_id=2, port=5001)

# Start server threads for both nodes
threading.Thread(target=node1.run_server).start()
threading.Thread(target=node2.run_server).start()

# Add peers
node1.add_peer(node2)
node2.add_peer(node1)

# Broadcasting a transaction from node1
node1.broadcast_transaction({'from': 'Alice', 'to': 'Bob', 'amount': 5})

# Node2 mines a block
node2.mine_block(miner_address="MinerAddress")
