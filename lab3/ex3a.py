from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3


ex3a_txout_scriptPubKey = [OP_2DUP,OP_ADD,211,OP_EQUALVERIFY,OP_SUB,3945,OP_EQUAL]
######################################################################
# OP_2DUP:赋值栈顶的两个元素 eg：[a,b]--OP_2DUP--[a,b,a,b]
# OP_ADD:取出栈顶的两个元素，相加后放回堆栈
# OP_EQUALVERIFY：栈顶两个项如果相等，那么将它们推出堆栈，脚本继续执行；如果不相等，脚本执行会立即停止，并返回一个失败的结果。
# OP_EQUAL:取出栈顶两个元素，如果相等则在堆栈中压入true，否则压入false

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0010
    txid_to_spend = (
        '3bc75b397d623b99b3d9366712ed4421e8adabf3f7d222b15b87c9f7eaf2ffb3')
    utxo_index = 3
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
