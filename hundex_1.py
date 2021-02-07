#Write a program which will find all such numbers which are divisible by 7
#but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
#Hints:  Consider use range(#begin, #end) method

l = []
x = 0
for i in range(2000,3200) :
    if (i%7==0) and (i%5!=0) :
        x = x + 1
        l.append(str(i))

print(','.join(l))
print('There are ', x, 'numbers div by 7, though not by 5, in the range')
