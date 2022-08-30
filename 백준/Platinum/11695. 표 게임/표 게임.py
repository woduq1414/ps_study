import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    sum(list(map(int, input().split())))
    for i in range(n)
]


nim_s = 0
for num in arr:
    nim_s ^= num
if nim_s == 0:
    print("ainta")
else:
    print("august14")
