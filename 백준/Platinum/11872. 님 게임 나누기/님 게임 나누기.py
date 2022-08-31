import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

nim_s = 0

for num in arr:


    if num <= 2:
        nim_s ^= num
    else:
        if num % 2 == 0:
            nim_s ^= num - 1
        else:
            nim_s ^= num + 1

if nim_s == 0:
    print("cubelover")
else:
    print("koosaga")