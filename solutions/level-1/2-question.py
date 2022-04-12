"""
Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
"""


# Soution One
def factorial(num):
    nums = range(1, num + 1)
    collect = 1
    i = 1
    while i < len(nums):
        collect *= nums[i]
        i += 1
    print(collect)


# Solutions Two // need explaination
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


factorial(5)
print(fact(5))
