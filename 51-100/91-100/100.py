"""
Write a program to solve a classic ancient Chinese puzzle:
编写一个程序来解决一个经典的中国古代谜题：

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
我们在一个农场的鸡和兔子中数了35个头和94条腿。我们有多少只兔子和多少只鸡?

Hint:
提示：

Use for loop to iterate all possible solutions.
使用for循环迭代所有可能的解决方案。
"""
# 本人答案
def solve_chickens_and_rabbits(total_heads, total_legs):
    for chickens in range(total_heads + 1):
        rabbits = total_heads - chickens
        if 2 * chickens + 4 * rabbits == total_legs:
            return chickens, rabbits
    return None
total_heads = 35
total_legs = 94
solution = solve_chickens_and_rabbits(total_heads, total_legs)
if solution:
    chickens, rabbits = solution
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")