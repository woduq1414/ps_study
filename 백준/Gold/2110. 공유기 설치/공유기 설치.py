import math
import sys
import copy

input = sys.stdin.readline

n, c = map(int, input().split())
arr = [ int(input()) for i in range(n) ]
arr.sort()

max_distance = (max(arr) - min(arr)) // (c - 1)
min_distance = 1
mid_distance = None

while min_distance <= max_distance:
    mid_distance = (max_distance + min_distance) // 2


    available_c = 1
    start_pos = arr[0]
    for num in arr[1:]:

        d = num - start_pos
        if d >= mid_distance:

            available_c += 1
            start_pos = num


    if available_c < c:
        max_distance = mid_distance - 1
    else:
        min_distance = mid_distance + 1

print(max_distance)






