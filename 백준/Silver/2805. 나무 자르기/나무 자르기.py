import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_len = max(arr)
min_len = 0
mid_len = None

while min_len <= max_len:

    mid_len = (max_len + min_len) // 2

    available_m = sum(
        filter(lambda x: x > 0, [length - mid_len for length in arr]))

    if available_m < m:
        max_len = mid_len - 1
    else:
        min_len = mid_len + 1

print(max_len)
