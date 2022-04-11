numbers = range(2000, 3201)
collect = []
for x in numbers:
    if x % 7 == 0 and x % 5 != 0:
        collect.append(str(x))

result = ", ".join(collect)
# print(result)

result2 = ", ".join([str(x)
                    for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0])

print(result2 == result)
