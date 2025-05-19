"""
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
请写断言语句来验证列表[2,4,6,8]中的每个数字都是偶数。

Hints:
提示：
Use "assert expression" to make assertion.
使用“assert-expression”进行断言。

"""

# 本人答案
list1=[2,4,6,8]
for i in list1:
    assert i%2==0, f"{i} is not an even number"