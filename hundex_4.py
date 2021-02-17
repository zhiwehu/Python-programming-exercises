#Write a program which accepts a sequence of comma-separated numbers
#from console and generate a list and a tuple which contains every number.
values = input("Enter Numbers SEPARATED BY COMMAS: ")
l = values.split(',')
print(l)
t = tuple(l)
print(t)

#Suppose the following input is supplied to the program: 34,67,55,33,12,98
#Then, the output should be: ['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
