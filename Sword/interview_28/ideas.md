# 面试题29. 顺时针打印矩阵
- **没做完**
- 出自剑指offer（第二版）

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

> 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
> 输出：[1,2,3,6,9,8,7,4,5]

## 思路一
先用len()函数确认有矩阵的行数，然后确认列数，一个一个附加到新的数组中去。

