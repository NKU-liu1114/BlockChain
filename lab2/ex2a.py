from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction

# 通过keygen.py生成三个账户，用来完成多方交易
# 1:Private key: cTVyCQZG3v2JgHZ2ABsj6B2DgGsKiEJbpzDfemybNkNyHbfzknJX
# Address: mvmt869z3AfCaWFkV9DAph7nasP3NfYJv7
# 2:Private key: cQUetkopdTNuZqxoScbmhfvzUhYn7CV5uB2gbfvVANyE8gP8HtDx
# Address: n3UmqKE5SNyhNsTFQAKLYGc21WHrAAWRE7
# 3:Private key: cR57Rs8Wx9g2KZ8AEonApVkYqd2GNihWeXpndx7tQXqrUkGANUsx
# Address: n2NB218KGrVsJRNzrLddUjp6331Y1LknCj

cust1_private_key = CBitcoinSecret(
    'cTVyCQZG3v2JgHZ2ABsj6B2DgGsKiEJbpzDfemybNkNyHbfzknJX')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cQUetkopdTNuZqxoScbmhfvzUhYn7CV5uB2gbfvVANyE8gP8HtDx')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cR57Rs8Wx9g2KZ8AEonApVkYqd2GNihWeXpndx7tQXqrUkGANUsx')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

# OP_2 <pubkey1> <pubkey2> <pubkey3> OP_3 OP_CHECKMULTISIG
# OP_2 表示需要 2 个签名来验证交易，而 <pubkey1> <pubkey2> <pubkey3> 则表示有 3 个可能的签名者。

ex2a_txout_scriptPubKey = [my_public_key,    # 银行公钥
OP_CHECKSIGVERIFY, 
OP_1,                                        # 将数字1压入堆栈
cust1_private_key.pub,
cust2_private_key.pub,
cust3_private_key.pub,       # 三个客户的公钥
OP_3,                        # 即需要三个人中的一个来签名
OP_CHECKMULTISIG
]

# OP_CHECKMULTISIG 首先从堆栈中取出一个数值，该数值表示多少个公钥将被提供（称为 n）。
# 接着，它从堆栈中取出 n 个公钥。
# 然后，又从堆栈中取出另一个数值，该数值表示为了成功验证，需要多少个签名（称为 m）。
# 最后，它从堆栈中取出 m 个签名。
# 验证签名:
# OP_CHECKMULTISIG 会尝试使用给定的公钥验证所有的签名。不是每一个公钥都必须有一个匹配的签名，但必须至少有 m 个有效的签名来满足条件。
# 结果推送:
# 如果至少有 m 个签名被成功验证，OP_CHECKMULTISIG 会把 1（true）压入堆栈。
# 如果验证失败，它会把 0（false）压入堆栈。

######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0014
    txid_to_spend = (
        '3bc75b397d623b99b3d9366712ed4421e8adabf3f7d222b15b87c9f7eaf2ffb3')
    utxo_index = 1
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
