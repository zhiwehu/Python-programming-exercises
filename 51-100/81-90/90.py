"""
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
通过使用列表理解,请编写一个程序来生成一个3*5*8的3D数组,其中每个元素都是0。

Hints:
提示：
Use list comprehension to make an array.
使用列表推导式来创建数组。
"""

# 本人答案
def generate_3d_array(dim1, dim2, dim3):
    return [[[0 for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
print(generate_3d_array(3, 5, 8))
