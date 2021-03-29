from flask import Flask, request
import json, requests

from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    index = blockchain.add_new_transaction(values)

    response = {'message': f'Transaction will be added to Block {index}'}

    return json.dumps(response)


@app.route('/mine', methods=['GET'])
def mine():
    index = blockchain.mine()

    response = {
        'message': "New Block Forged",
        'index': index,
    }

    return json.dumps(response)


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []

    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    response = {
        'chain': chain_data,
        'length': len(chain_data),
    }

    return json.dumps(response)


app.run(debug=True, port=5000)
