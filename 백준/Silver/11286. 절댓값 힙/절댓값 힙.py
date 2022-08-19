import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])

    else:
        heapq.heappush(q, (abs(x), x))


