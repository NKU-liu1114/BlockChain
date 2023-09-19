## 实验说明


>Ex1和Notice为实验指导内容和要求,主要完成拆分可消费的输出和发送回faucet两个任务 \
config.py存储需要用到的数据，keygen.py用于生成私钥、地址\
account&password.txt保存账户的账号（Address）和私钥（密码）\
运行split_test_coins.py，将输出分为多份，运行ex1.py将bitcoin发送回faucet\
split.png和send to faucet.png是在BTC浏览器上查询到的交易记录截图\
result_send_to_faucet.txt保存送回faucet后的事务输出，result_split.txt保存分为多份消费的事务输出\
\


## 实验流程
>在keygen生成Address，txid和私钥后，首先补充config.py的相关信息和参数，此时填写的txid即为keygen.py得到的txid，之后在split.py中键入相关参数，输出得到事务哈希值，在ex1.py中用此哈希值作为txid完成事务。最后在BTC浏览器上搜索两个事务的哈希值，获得交易记录截图。注意细节： utxo_index需要在BTC浏览器上查询是第几个输出值。



