import sys

input = sys.stdin.readline

n , k = map(int, input().split())

arr = [ int(input()) for i in range(n)]

max_len = sum(arr) // k
min_len = 1
mid_len = None

while min_len <= max_len:

    mid_len = (max_len + min_len) // 2

    available_k = sum([length // mid_len for length in arr])
    if available_k < k:
        max_len = mid_len - 1
    else:
        min_len = mid_len + 1

print(max_len)