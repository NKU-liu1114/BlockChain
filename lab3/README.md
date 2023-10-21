## 实验流程
- 运行ex3a.py(引用的UTXO为lab1中生成的10个输出，因为在lab1和lab2中已经使用了0,1,2号输出，故本次实验utxo_index取3)，生成tx_id，在ex3b.py中花费ex3a.py的输出，引用的UTXO为ex3a.py生成的tx_id,此时utxo_index取0，完成交易。

## 实验说明
- 实验中数学谜题的值取学号前三位211，后四位3946-1，保持奇偶性。在ScriptSig中将求解出的两个值推送到栈上。ScriptPubKey将栈上的两个值先进行复制，相加后与求解的目标值相比较，之后再将栈上原始的两个值进行相减，如果也等于目标值，则将true返回栈中。脚本执行时ScriptSig结合ScriptPubKey一起执行，完成验证。
