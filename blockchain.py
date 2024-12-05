from block import Block
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(len(self.chain), self.get_latest_block().hash, time.time(), self.pending_transactions)
        block.mine_block(self.difficulty)
        print("Block successfully mined")
        self.chain.append(block)
        self.pending_transactions = [{"from": None, "to": mining_reward_address, "amount": self.mining_reward}]

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
