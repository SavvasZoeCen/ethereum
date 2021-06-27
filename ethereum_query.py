from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if not w3.isConnected():
    print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx0 = w3.eth.get_transaction(tx)   #YOUR CODE HERE
    return tx0

# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    txn = w3.eth.get_transaction(tx)
    gas_price = txn['gasPrice'] #YOUR CODE HERE
    return gas_price

def get_gas(tx):
    rec = w3.eth.get_transaction_receipt(tx)
    gas = rec['gasUsed'] #YOUR CODE HERE
    return gas

def get_transaction_cost(tx):
    tx_cost = get_gas_price(tx) * get_gas(tx) #YOUR CODE HERE
    return tx_cost

def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    transactions = block['transactions']
    block_cost = 0  #YOUR CODE HERE
    for tx in transactions:
      block_cost += get_transaction_cost(tx)
    return block_cost

# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    block = w3.eth.get_block(block_num)
    transactions = block['transactions']
    max_tx = 0
    for tx in transactions:
      max_tx = max(max_tx, get_transaction_cost(tx))
    
    #max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    return max_tx
