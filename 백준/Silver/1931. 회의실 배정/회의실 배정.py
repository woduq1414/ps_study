import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

m = -1
c = 0
for a, b in arr:
    if a >= m:
        m = b
        c += 1
print(c)
