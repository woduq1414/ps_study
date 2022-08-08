import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(0, i):
        arr[j][i] += arr[i][j]
        arr[i][j] = 0

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end=" ")
#     print()

min_value = 10 ** 10



def func(lis, output, c):
    if c == 0:
        # print(*output)

        #################
        result_a = sum([arr[0][x] for x in output]) + func2(output, [], 2, 1)


        global n
        output_b = [x for x in range(1, n) if x not in output]
        result_b = func2(output_b, [], 2, 1)

        global min_value
        result_diff = abs(result_a - result_b)
        if result_diff < min_value:
            min_value = result_diff

        return

    for num in lis:

        if len(output) > 0 and num <= output[-1]:
            continue

        temp = lis[:]
        temp.remove(num)

        func(temp, output + [num], c - 1)


def func2(lis, output, c, c2):
    result = 0

    global arr

    if c == 0:
        return arr[output[0]][output[1]]

    for num in lis:

        if len(output) > 0 and num <= output[-1]:
            continue




        temp = lis[:]

        temp.remove(num)

        result += func2(temp, output + [num], c - 1, c2 + 1)
    return result


func(list(range(1, n)), [], n / 2 -1)
print(min_value)