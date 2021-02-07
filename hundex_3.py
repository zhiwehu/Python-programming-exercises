#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
inum = input('Enter number: ')
try :
    num = int(inum)
except :
    print('Please enter a NUMBER, try again.')
    exit()

dsqr = dict()
i = num + 1
#print(i)
while i > 1 :
    #if i == 1 : break
    #else :
    i = i - 1
    s = i*i
    #print(i)
    #print(s)
    dsqr[i] = s

print(dsqr)







#Suppose the following input is supplied to the program: 8
#Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
