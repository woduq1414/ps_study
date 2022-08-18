import math
import sys
import copy

input = sys.stdin.readline

n, k = int(input()), int(input())

max_num = n * n
min_num = 1

while min_num <= max_num:

    mid_num = (min_num + max_num) // 2


    t = sum([ min(n, mid_num // i) for i in range(1, n + 1) ])


    if t < k:
        min_num = mid_num + 1
    else:
        max_num = mid_num - 1


print(max_num + 1)