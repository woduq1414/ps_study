import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())

arr = list(map(int, input().split()))
len_arr = [0] * n
chain_arr = [[] for _ in range(n)]

for i in range(n - 1, -1, -1):

    if i == n - 1:
        len_arr[i] = 1
        chain_arr[i] = [i]
    else:
        min_index = None
        for j in range(i + 1, n):
            if arr[j] > arr[i] and (
                    min_index is None or len_arr[j] > len_arr[min_index]):
                min_index = j

        if min_index is None:
            len_arr[i] = 1
            chain_arr[i] = [i]
        else:
            len_arr[i] = len_arr[min_index] + 1
            chain_arr[i] = [i] + chain_arr[min_index]

max_len = max(len_arr)

print(max_len)

for i in range(n):
    if len(chain_arr[i]) == max_len:
        print(*[arr[k] for k in chain_arr[i]], sep=" ")
        break
