from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

# Initialize the Blockchain
blockchain = Blockchain()

# Endpoint to mine a block
@app.route('/mine', methods=['GET'])
def mine_block():
    blockchain.mine_pending_transactions("MinerAddress")
    return jsonify({
        "message": "A new block has been mined!",
        "block": blockchain.chain[-1].__dict__
    }), 200

# Endpoint to create a new transaction
@app.route('/transactions/create', methods=['GET'])
def create_transaction():
    from_addr = request.args.get('from')
    to_addr = request.args.get('to')
    amount = request.args.get('amount')

    if not from_addr or not to_addr or not amount:
        return jsonify({"message": "Missing transaction fields"}), 400

    transaction = {"from": from_addr, "to": to_addr, "amount": int(amount)}
    blockchain.create_transaction(transaction)
    return jsonify({"message": "Transaction created", "transaction": transaction}), 201

# Endpoint to return the blockchain
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = [block.__dict__ for block in blockchain.chain]
    return jsonify({"chain": chain_data, "length": len(chain_data)}), 200

# Endpoint to validate the blockchain
@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = blockchain.is_chain_valid()
    if is_valid:
        return jsonify({"message": "Blockchain is valid!"}), 200
    else:
        return jsonify({"message": "Blockchain is not valid!"}), 400

if __name__ == '__main__':
    app.run(port=5000)
