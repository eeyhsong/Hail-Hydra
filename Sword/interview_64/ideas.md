#  面试题64. 求1+2+3+...+n

求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

## 思路一
给定一个输入n

最直接的方法当然是自加了，不用for？you kidding

## 思路二
上底+下底和乘高除以二，也就是求平均数的方法，也就是题目限制的乘除法

## 思路三
已经在朝着正确的方向去了 

递归求解，```n += sumNums(n-1)```

但对于递归，存在一个问题需要注意：python无法在类内调用类，而函数体本身可以（看到一种解释：函数体不只是根据定义执行，而类体是根据定义执行的）。

如何调用请参考Solution3.py，定义了```__init__()```

## 思路四
不让用循环，不让用循环、不让用条件，那考虑下逻辑符号实现递归终止？

逻辑运算符```&&```和```||```和```非!```具有短路效应
> python中and：若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A and B 为 false

> python中or： 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A or B 为 true

## 思路五
很巧妙的思路，直接用python中的range函数生成一个整数列表后用sum函数求和。注意数据类型就是range类，复杂度是O(n)。

## 复杂度分析（思路四）
时间复杂度，要递归n次，则为O(n)；

空间复杂度，递归深度为n，则为O(n)。





