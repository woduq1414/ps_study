import sys
input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())

s = 0
nim_s = 0

for num in arr:
    nim_s ^= num
    s += num

if n == s:
    if n % 2 != 1:
        print("koosaga")
    else:
        print("cubelover")
else:
    if nim_s != 0:
        print("koosaga")
    else:
        print("cubelover")