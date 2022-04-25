# Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# My code (incomplete)

# n = int(input("Please input an integer: "))
# i = 1

# def factorial(n):
#     for x in range(1, n):
#         i = i *= x 
#     return x 

# print(factorial(n))

# Answer Code

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))

# Alternative valid code

n = int(input("Please input an integer: "))
fact = 1

for x in range(1, n + 1):
    fact = fact * x 

print(fact)


# So I couldn't figure this one out but I was close to the 2nd solution, which I found to be the more intuitive one.
# My error was trying to apply the assignment operator *= rather than simply multiplication.  The reason the multiplier works
# is because the variable "fact" is initially assigned (=) the value of 1 then, in the "for" loop, is assigned the value 
# "fact * x" for every x between 1 and n+1.  

# So for example: 
# for n=5 the code will run: fact = 1 * 1 = 1, then fact = 1 * 2 = 2, then fact = 2 * 3 = 6, then fact = 6 * 4 = 24,
# then fact = 24 * 5 = 120. 

# The actual provided answer code is slightly different and rather than iterating as in the for loop uses a process called
# "recursion", this is when a function calls itself until some closing condition.  In this case the function first 
# checks if x == 0 and if so will return the value of 1. If x != 0 then the function returns x mulitplied by the return 
# value of the same function but with input of x - 1.

# Using the same example again:
# for x=5 the code will run: 
# fact(5) --> x != 0 so x = 5 * fact(x - 1), then it will run and repeat the final line for x - 1 until x == 0
# so the code will essentially show: 5 * 4 * 3 * 2 * 1 * 1, the last 1 is where x == 0 and the recursion stops. 

# Another way to visualise the recursive function:
# for x=5:
# x * fact(x-1) which returns x-1 * fact((x-1)-1) so:
# x * (x-1) * fact((x-1)-1)) = 5 * 4 * fact(4-1) so:
# x * (x-1) * ((x-1)-1) * fact(((x-1)-1)-1) = 5 * 4 * 3 * fact(3-1) 
# etc. until x eventually == 0 and returns the result 1.