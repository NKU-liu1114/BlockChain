from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import P2PKH_scriptPubKey
from ex3a import ex3a_txout_scriptPubKey


######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.0005
txid_to_spend = '5c6eb82716ac6febc11de558ccf386236315703d7618138f67ac2a1beb92bc95' # ex3a.py生成的tx哈希
utxo_index = 0
######################################################################


txin_scriptPubKey = ex3a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 3a.
txin_scriptSig = [2078,-1867]
# x+y=211,x-y=3945
# 为了解锁scriptPubkey,需要将问题的答案推到解锁脚本的堆栈中，之后结合scriptPubkey一起执行
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey)
print(response.status_code, response.reason)
print(response.text)
