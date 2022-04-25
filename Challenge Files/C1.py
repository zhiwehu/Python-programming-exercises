# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# My code:

for x in range(2000, 3201):
     a = x / 7
     b = x / 5
     if a - int(a) == 0 and b - int(b) != 0:
        print(f"{x},", end="")


#Answer code:

# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(','.join(l))


# Both of the above perform the same function, however, the difference between them is the use of the modulus operator in the
# answer code.  My code subtracts an int value of x/7 (i.e. 10) from the float value of x/7 (i.e. 10.0) and if the result is 
# zero then this means that x is divisible by 7 (as float(x) = int(x)) and therefore there is no remainder. 

# The modulus "%" operator essentially performs this function automatically, it returns the remainder of a given division, 
# i.e. if x is divisible by 7 then x%7 == 0.