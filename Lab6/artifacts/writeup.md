Name: [lgm]

## Question 1

In the following code-snippet from `Num2Bits`, it looks like `sum_of_bits`
might be a sum of products of signals, making the subsequent constraint not
rank-1. Explain why `sum_of_bits` is actually a _linear combination_ of
signals.

```
        sum_of_bits += (2 ** i) * bits[i];
```

## Answer 1

上式仍满足一阶约束，这是因为 `2**i` 是一个常数，乘以信号量 bits[i] 后满足一阶约束要求（即没有出现信号量与信号量相乘的情形）。所以 `sum_of_bits` 是一个信号量的线性组合，即将每个比特位按照 2**i 的权重累加起来，得到数字。

## Question 2

Explain, in your own words, the meaning of the `<==` operator.

## Answer 2

`<==` 是一个赋值运算符，用于将表达式的结果赋值给信号(signal)，同时添加一个约束。也可以把 `<==` 操作分解成 `<--` 和 `===`，前者只赋值不加约束，后者只加约束不赋值。`<==` 将两个操作合并在了一起。


## Question 3

Suppose you're reading a `circom` program and you see the following:

```
    signal input a;
    signal input b;
    signal input c;
    (a & 1) * b === c;
```

Explain why this is invalid.

## Answer 3

circom语言特性中没有位运算，即不支持类似于C/C++的按位与操作（&）
