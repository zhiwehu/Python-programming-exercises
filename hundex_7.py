#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
#The element value in the i-th row and j-th column of the array should be i*j
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example Suppose the following inputs are given to the program: 3,5
values = input('Please Enter Numbers separated by Comma: ')

l = list() #array list
sl = list() #sub list
i = 0 # i-dimensional counter
j = 0 # j-dimensional counter
d = (values.split(',')) # creating an input list
X = int(d[0])
Y = int(d[1])
while i < X : # creating X-1 arrays
    while j < Y : # creating the Y-1 array
        y = i * j
        j = j + 1
        sl.append(y) # creating the Y arrays
    j = 0 # to reset the counter back to 0 on each iteration
    #print(sl) # print check
    i = i + 1
    l.append(sl)
    sl = list() # RESETING Y array LIST BACK TO 0

print(l)
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
