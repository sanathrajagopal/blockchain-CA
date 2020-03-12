import time
from web3 import Web3, HTTPProvider
from hexbytes import HexBytes
import contract_abi 

contract_address     = '0x63a14d2D4fEBaB99e42D15183324397864b38816'
wallet_private_key   = 'c417fa9c4a8dedf17345bb709f8ad2c6d283bf3fd189403065abfcbe37d09c60'
wallet_address       = '0x29CA6bDd9FDf408dc5b8dAC5a0b62a92fb06f975'
w3 = Web3(HTTPProvider('https://ropsten.infura.io/v3/e988a4ab830e4a7da087f03aa3dbe036'))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)
#w3.eth.enable_unaudited_features()


def send_ether_to_contract(amount_in_ether):

    amount_in_wei = w3.toWei(amount_in_ether,'ether')
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = {
            'to': contract_address,
            'value': amount_in_wei,
            'gas': 200000,
            'gasPrice': w3.toWei('3.9', 'gwei'),
            'nonce': nonce,
            'chainId': 3
    }

    signed_txn = w3.eth.account.signTransaction(txn_dict, wallet_private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_hash = txn_hash.hex()
    txn_receipt = None
    count = 0
    while txn_receipt is None and (count < 30):
        try:
            txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
        except:
            time.sleep(10)
            txn_receipt = None
        else:
            print(txn_receipt)
            break

    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

def approve_publisher(w_addr):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.ApprovePublisher(w_addr).buildTransaction({
        'chainId':3,
        'gas':400000,
        'gasPrice':w3.toWei('3.9','gwei'),
        'nonce':nonce,
    })
    signed_txn = w3.eth.account.signTransaction(txn_dict,private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = None

    count = 0
    while tx_receipt is None and (count<30):
        try:
            txn_receipt = w3.eth.getTransactionReceipt(result)
        except:
            time.sleep(10)
            txn_receipt = None
        else:
            print(txn_receipt)
            break
    
    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}


def check_whether_address_is_approved(address):
    return contract.functions.isApproved(address).call()

def get_public_key(publisher_address):
    return contract.functions.get_pubkey(publisher_address).call()

def publish_public_key(pubkey,publisher_address):
    nonce = w3.eth.getTransactionCount(wallet_address)
    txn_dict = contract.functions.broadcastPublicKey(pubkey,publisher_address).buildTransaction({
        'chainId':3,
        'gas':600000,
        'gasPrice':w3.toWei('3.9','gwei'),
        'nonce':nonce,
    })
    signed_txn = w3.eth.account.signTransaction(txn_dict,private_key=wallet_private_key)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = None

    count = 0
    while tx_receipt is None and (count<30):
        try:
            txn_receipt = w3.eth.getTransactionReceipt(result)
        except:
            time.sleep(10)
            txn_receipt = None
        else:
            print(txn_receipt)
            break
    
    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    return {'status': 'added', 'txn_receipt': txn_receipt}

#print(dir(contract))
#send_ether_to_contract(0.06)
#approve_publisher('0x62a3F16Aed1B029A76768b262E9ED1c2A2952FC0')
print(check_whether_address_is_approved('0x62a3F16Aed1B029A76768b262E9ED1c2A2952FC0'))
#publish_public_key('4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454132616b624f43385248704a4f4f4b682b6f48396c7564646e30536b504c626b745a46436b2b756f376f74386f3976536f2b6531746363423859666a783932313251796e4f7141386e6c59486a375938683876535663387038365632744e593943376f304f4263513165624f65374b5a4f5546423567724b72592b44775433306738382b33576653424a4f654b43386f6a5134792f4371395735304a37786371574379425864564d494b434c3665695865396159443467515853537a4261754c2b6d6c587779583533666f7848666974784f35773739436a344b414773666b424639736c72334a51706f4e6f4d2f542b4b4b7072726f7852506e654450394159336d55694645744d50355149595132696543304f435050396545634a6c75557850474236714476786c4941757836415143454944764b4c34743368552b51563839713777544f4a65542f41474f6b5a716657394a317077494441514142','0x62a3F16Aed1B029A76768b262E9ED1c2A2952FC0')
print(get_public_key('0x62a3F16Aed1B029A76768b262E9ED1c2A2952FC0'))
