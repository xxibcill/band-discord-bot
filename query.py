import os
from urllib import response

from pyband.client import Client
from pyband.transaction import Transaction
from pyband.wallet import PrivateKey
from pyband.obi import PyObi

from pyband.proto.cosmos.base.v1beta1.coin_pb2 import Coin
from pyband.proto.oracle.v1.tx_pb2 import MsgRequestData
from pyband.proto.cosmos.bank.v1beta1.tx_pb2 import MsgSend
from pyband.proto.cosmos.bank.v1beta1.tx_pb2 import MsgMultiSendResponse
from google.protobuf.json_format import MessageToJson

MNEMONIC = "brown kite lady anger income eager left since brown cruise arch danger"
# MNEMONIC = "danger kite lady anger income eager left since brown cruise arch danger"

grpc_url = "laozi1.bandchain.org" # ex.laozi-testnet5.bandchain.org(without https://)
client = Client(grpc_url)

def get_account(private_key):
    # Step 1
    public_key = private_key.to_public_key()
    sender_addr = public_key.to_address()
    sender = sender_addr.to_acc_bech32()
    account = client.get_account(sender)
    return account

def make_request_tx(sender):
    # OBI encode calldata
    obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
    test_input = { "symbols": ['ETH','USDC'], "multiplier": 100 }
    calldata = obi.encode_input(test_input)

    # Step 3
    request_msg = MsgRequestData(
        oracle_script_id=37,
        calldata=calldata,
        ask_count=16,
        min_count=10,
        client_id="BandProtocol",
        fee_limit=[Coin(amount="100", denom="uband")],
        prepare_gas=50000,
        execute_gas=200000,
        sender=sender,
    )

    account = client.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = client.get_chain_id()

    # Step 4
    txn = (
        Transaction()
        .with_messages(request_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(2000000)
        .with_fee(fee)
        .with_memo("")
    )

    return txn

def make_sendcoin_tx(sender,reciever,amount):
    # band10h9pfuddwxjhdjxv2pk7mselmz4m50xydsk003
    send_msg = MsgSend(
       from_address = sender,
       to_address = reciever,
       amount = [Coin(amount=str(amount), denom="uband")]
    )

    account = client.get_account(sender)
    account_num = account.account_number
    sequence = account.sequence

    fee = [Coin(amount="0", denom="uband")]
    chain_id = client.get_chain_id()

    # Step 4
    txn = (
        Transaction()
        .with_messages(send_msg)
        .with_sequence(sequence)
        .with_account_num(account_num)
        .with_chain_id(chain_id)
        .with_gas(2000000)
        .with_fee(fee)
        .with_memo("")
    )

    return txn




def sign_tx(txn,private_key):
    public_key = private_key.to_public_key()
    sign_doc = txn.get_sign_doc(public_key)
    signature = private_key.sign(sign_doc.SerializeToString())
    tx_raw_bytes = txn.get_tx_data(signature, public_key)
    return tx_raw_bytes

def ger_ref_data(pairs):
    return client.get_reference_data(pairs, 10, 16)

def get_oracle_script(id):
    return client.get_oracle_script(id)
    
def get_data_source(id):
    return client.get_data_source(id)

def get_account(address):
    return client.get_account(address)

def get_latest_block():
    return client.get_latest_block()

# band1pdvm6paaenlelmga2qkr50thpkrzwxy3gsr4xs
# band1w2fh72f6u76l8pk5vewzqg30aztflthg5ufrst
# band1vxr8awcjrdc3ksxapla59lj47lpr6yne02pfz7
# band14d07sfjyd3e3n9qd0lzu3ncfuws69daedjvly2
# band18t8562duj4gtcqcx8hpcj9ykurajzsrlxm7tg9
# band1gy74ce5aqfc9matjkxl8ju5y4ezgf939m9dqg7
# band10wyzm2z56u7kz6jwdsd6amg0v2wpws5f2tzlc3
# band16lq4m5d2h5wvy3vhvg2ct2gdkvhzwfnu9xprkx
# band189rh34afdvvr3mlyw2c98uqksz8wqt7dzavma0
# band1868crmeh20apds2t2rnqasyugu67pve5a498vs

# if __name__ == "__main__":
#     grpc_url = "laozi-testnet5.bandchain.org" # ex.laozi-testnet5.bandchain.org(without https://)
#     client = Client(grpc_url)

#     private_key = PrivateKey.from_mnemonic(MNEMONIC,f"m/44'/118'/0'/0/{0}")
#     sender = private_key.to_public_key().to_address().to_acc_bech32()
#     print(sender)

#     send_msg = MsgMultiSendResponse(
#        from_address = sender,
#        to_address = "band1868crmeh20apds2t2rnqasyugu67pve5a498vs",
#        amount = [Coin(amount=str(amount), denom="uband")]
    # )



    # tx = make_sendcoin_tx(sender,"band1pdvm6paaenlelmga2qkr50thpkrzwxy3gsr4xs",8900000)
    # tx_raw_bytes = sign_tx(tx,private_key)

    # res = client.send_tx_sync_mode(tx_raw_bytes)
    # print(res.txhash)
    # print(client.get_request_id_by_tx_hash(res.txhash))



