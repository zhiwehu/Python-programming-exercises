"""
Please generate a random float where the value is between 5 and 95 using Python math module.
请使用Python数学模块生成一个值在5到95之间的随机浮点数。

Hints:
提示：

Use random.random() to generate a random float in [0,1].
使用random.random()在[0,1]中生成随机浮点数。
"""
# 本人答案
import random
print (random.random()*90 + 5)