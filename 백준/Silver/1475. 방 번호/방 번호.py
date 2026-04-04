import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

s = input()

arr = [0] * 10
for c in s:
    arr[int(c)] += 1

r = max(max(arr[:6] + arr[7:9]), (arr[6] + arr[9] + 1) // 2)

print(r)

