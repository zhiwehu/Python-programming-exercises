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
