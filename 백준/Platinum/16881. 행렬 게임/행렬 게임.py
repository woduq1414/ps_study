import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))[::-1]
    for i in range(n)
]

nim_s = 0

for i in range(n):

    g_num = arr[i][0]


    for j in range(1, m, 1):
        if g_num >= arr[i][j]:
            g_num = arr[i][j] - 1
        else:
            g_num = arr[i][j]


    nim_s ^= g_num
    # print(g_num)

if nim_s == 0:
    print("cubelover")
else:
    print("koosaga")
