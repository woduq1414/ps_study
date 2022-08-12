import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())

arr = list(map(int, input().split()))

len_arr = [1] * n
len_arr[0] = 1
for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]:
            len_arr[i] = max(len_arr[j] + 1, len_arr[i])

print(max(len_arr))

