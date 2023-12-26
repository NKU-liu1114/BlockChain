include "./mimc.circom";

/*
 * IfThenElse sets `out` to `true_value` if `condition` is 1 and `out` to
 * `false_value` if `condition` is 0.
 *
 * It enforces that `condition` is 0 or 1.
 *
 */
template IfThenElse() {
    signal input condition;
    signal input true_value;
    signal input false_value;
    signal output out;

    
    condition * (1 - condition) === 0;

    signal diff <-- true_value - false_value;

    out <== condition * diff + false_value;

}

/*
 * SelectiveSwitch takes two data inputs (`in0`, `in1`) and produces two ouputs.
 * If the "select" (`s`) input is 1, then it inverts the order of the inputs
 * in the ouput. If `s` is 0, then it preserves the order.
 *
 * It enforces that `s` is 0 or 1.
 */
template SelectiveSwitch() {
    signal input in0;
    signal input in1;
    signal input s;
    signal output out0;
    signal output out1;

    s * (1 - s) === 0;


    component firstOutput = IfThenElse();
    firstOutput.condition <== s;
    firstOutput.true_value <== in1;
    firstOutput.false_value <== in0;

    component secondOutput = IfThenElse();
    secondOutput.condition <== s;
    secondOutput.true_value <== in0;
    secondOutput.false_value <== in1;

    out0 <== firstOutput.out;
    out1 <== secondOutput.out;
}

/*
 * Verifies the presence of H(`nullifier`, `nonce`) in the tree of depth
 * `depth`, summarized by `digest`.
 * This presence is witnessed by the additional inputs `sibling` and
 * `direction`, which have the following meaning:
 *   sibling[i]: the sibling of the node on the path to this coin
 *               commitment at the i'th level from the bottom.
 *   direction[i]: whether that sibling is on the left.
 *       The "sibling" keys correspond directly to the siblings in the
 *       SparseMerkleTree path.
 *       The "direction" keys the boolean directions from the SparseMerkleTree
 *       path, casted to string-represented integers ("0" or "1").
 */
template Spend(depth) {
    signal input digest;
    signal input nullifier;
    signal private input nonce;
    signal private input sibling[depth];
    signal private input direction[depth];

    // 保存路径上的哈希值
    component computed_hash[depth + 1];
    // 调模版
    computed_hash[0] = Mimc2();
    // H(nullifier||nonce)
    computed_hash[0].in0 <== nullifier; 
    computed_hash[0].in1 <== nonce;
    // 保存经过switch操作后的值，输出拿给Mimc2来哈希
    component switches[depth];

    for (var i = 0; i < depth; ++i) {
        // 调模版
        switches[i] = SelectiveSwitch();
        // 如果direction[i]为1，则sibling[i]在当前节点左边
        // 则in0输入为当前节点哈希，in1为sibling[i]
        // 根据SelectiveSwitch逻辑会交换两个输入然后赋值给两个输出
        switches[i].in0 <== computed_hash[i].out;
        switches[i].in1 <== sibling[i];
        switches[i].s <== direction[i];
        // 调模版
        computed_hash[i + 1] = Mimc2();
        // 依次赋值switch操作后的输出值
        computed_hash[i + 1].in0 <== switches[i].out0;
        computed_hash[i + 1].in1 <== switches[i].out1;
    }
    // 计算出的根节点哈希应该与输入的 digest 相同，满足约束
    computed_hash[depth].out === digest;
}