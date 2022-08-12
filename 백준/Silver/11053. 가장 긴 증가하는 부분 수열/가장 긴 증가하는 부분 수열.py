import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())

arr = list(map(int, input().split()))
len_arr = [0] * n


for i in range(n - 1, -1, -1):

    if i == n - 1:
        len_arr[i] = 1
    else:
        min_index = None
        for j in range(i + 1, n):
            if arr[j] > arr[i] and (
                    min_index is None or len_arr[j] > len_arr[min_index]):
                min_index = j

        if min_index is None:
            len_arr[i] = 1
        else:
            len_arr[i] = len_arr[min_index] + 1

print(max(len_arr))
