import sys

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

nim_s = 0
for num in arr:
    nim_s ^= num
if nim_s == 0:
    print("cubelover")
else:
    print("koosaga")