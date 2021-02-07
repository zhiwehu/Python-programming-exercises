#Write a program which can compute the factorial of a given numbers.
def fact(x) :
    n = 0
    i = x - n
    while i >= 2 :
        n = n + 1
        #print(n)
        i = i - 1
        #print(i)
        x = x * i
    return x

#The results should be printed in a comma-separated sequence on a single line.
inum = input('Insert Number: ')
try :
    num = int(inum)
except :
    print('Only Numbers valid.')
    exit()

y = fact(num)
print('the factorial of: ', inum, 'is', y)

# Suppose the following input is supplied to the program: 8
#Then, the output should be: 40320

#it should be assumed to be a console input.
