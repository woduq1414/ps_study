str = input()

substr_list = [
''
] * len(str)
result = 0
for i in range(len(str)):

    for j in range(len(str) - i):
        substr_list[j] += str[j + i]

    result += len(set(substr_list[:len(str) - i]))

    # print(substr_list)
# print(substr_list)
print(result)