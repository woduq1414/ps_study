import sys

input = sys.stdin.readline

n = int(input())

g_arr = [0,0,1,1]


for i in range(4, n + 1, 1):

    group = [0] * 1001
    for j in range(i - 2):
        group[g_arr[j] ^ g_arr[i - 2 - j]]= 1
    g_num = 0
    while group[g_num]== 1:
        g_num += 1

    g_arr.append(g_num)


print([1,2][g_arr[n]== 0])