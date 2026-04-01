str = input()

substr_list = [

]
result = 0
for i in range(len(str)):
    substr_list.append([])

    if i == 0:
        for j in range(len(str)):
            substr_list[0].append(str[j])

    else:
        for j in range(len(str) - i):
            substr_list[i].append(substr_list[i - 1][j] + str[j + i])

for i in range(len(str)):
    result += len(set(substr_list[i]))

# print(substr_list)
print(result)