import sys
input = sys.stdin.readline
n = int(input())
arr = map(int, input().split())

nim_s = 0

for num in arr:
    nim_s ^= num

if n == 1:
    print("koosaga")
else:
    if nim_s == 0:
        print("cubelover")
    else:
        print("koosaga")