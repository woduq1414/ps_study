import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

new_arr = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        new_arr[j][i] = arr[i][j]

arr = new_arr


cum_arr = [[0] * n for i in range(n)]
cum_arr2 = [[0] * n for i in range(n)]

cum_arr[0] = arr[0][:]

for i in range(1, n):
    for j in range(0, n):
        cum_arr[i][j] = cum_arr[i - 1][j] + arr[i][j]

for i in range(n):
    cum_arr2[i][0] = cum_arr[i][0]

for i in range(n):
    for j in range(1, n):
        cum_arr2[i][j] = cum_arr2[i][j - 1] + cum_arr[i][j]


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    print(cum_arr2[y2][x2] - ((cum_arr2[y2][x1 - 1] if x1 >= 1 else 0) + (
        cum_arr2[y1 - 1][x2] if y1 >= 1 else 0) - (cum_arr2[y1 - 1][
                                                       x1 - 1] if x1 >= 1 and y1 >= 1 else 0)))
