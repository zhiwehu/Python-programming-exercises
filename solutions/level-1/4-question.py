"""
Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
"""

# Solution without input


# def print_list_tuple(*string):
#     print((string))
#     print([x for x in string])


# print_list_tuple(34, 67, 55, 33, 12, 98)


# Solution w/ input


def input_list_tuple(value):
    arr = [int(x) for x in value.split(", ")]
    tup = tuple(arr)
    print(arr)
    print(tup)


value = input("Enter nums separated by commas: ")

input_list_tuple(value)
