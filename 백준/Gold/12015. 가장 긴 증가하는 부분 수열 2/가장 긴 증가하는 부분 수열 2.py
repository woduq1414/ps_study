import sys

import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

c = [10 ** 9] * (n + 1)
c[0] = -1
c[1] = arr[0]
longest_len = 1

for i, num in enumerate(arr[1:]):

    if c[longest_len] < num:
        c[longest_len + 1] = num
        longest_len += 1
    else:
        idx = bisect.bisect_left(c, num)
        c[idx] = num

print(longest_len)
