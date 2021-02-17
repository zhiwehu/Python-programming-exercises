#Write a program which accepts a sequence of numbers from console
#and generate a list and a tuple which contains every number.
l = list()
while True :
    values = input("Enter Numbers: ")
    if values == 'done' :
        print('Done')
        break
    else :
        l.append(values)

print(l)
t = tuple(l)
print(t)

#Suppose the following input is supplied to the program: 34,67,55,33,12,98
#Then, the output should be: ['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
