"""

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""

def f ():
    mystr = ""

    start = 2000
    while start % 7 != 0:
        start +=1

    else:
        for v in range(start, 3201, 7):
            if not v % 5 == 0:
                mystr += str(v) + ","
    return mystr

print(f())