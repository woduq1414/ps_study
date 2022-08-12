import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())

arr = list(map(int, input().split()))

len_arr, len_arr2 = [1] * n, [1] * n

len_arr[0] = 1
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            len_arr[i] = max(len_arr[j] + 1, len_arr[i])

arr.reverse()

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            len_arr2[i] = max(len_arr2[j] + 1, len_arr2[i])

len_arr2.reverse()


print(max([a + b for a, b in zip(len_arr, len_arr2)]) - 1)

