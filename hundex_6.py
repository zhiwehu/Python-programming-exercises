#Write a program that calculates and prints the value
#should be input to your program in a comma-separated sequence.
values = input('Please Enter Numbers separated by Comma: ')
#according to the given formula: Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H: C is 50. H is 30.
l = values.split(',')
ls = list()
for D in l :
    D = float(D)
    C = 50
    H = 30
    Q = ((2 * C * D)/H)**(1/2)
    ls.append(str(int(Q)))#it should be rounded off to its nearest value

#print(ls)
delimiter = ','
r = delimiter.join(ls)
print(r)

#print(','.join(ls))
