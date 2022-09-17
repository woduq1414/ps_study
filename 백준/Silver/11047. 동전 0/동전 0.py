import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

s = 0

for cost in reversed(arr):
    q, r = divmod(k, cost)
    s += q
    k = r
print(s)