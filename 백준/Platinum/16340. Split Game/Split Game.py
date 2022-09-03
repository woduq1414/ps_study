import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

g_arr = [0, 0, 1]

for i in range(3, max(arr) + 1, 1):

    group = [0] * 2001
    for j in range(1, i, 1):

        if (i // j) % 2 == 0:
            t = g_arr[i % j]
        else:
            t = g_arr[j] ^ g_arr[i % j]

        group[t] = 1
    g_num = 0
    while group[g_num] == 1:
        g_num += 1

    g_arr.append(g_num)

nim_s = 0

for num in arr:
    nim_s ^= g_arr[num]

print(["First", "Second"][nim_s == 0])
