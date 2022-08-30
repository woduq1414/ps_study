import sys

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

def get_grundy_num(num):
    if num == 0:
        return 0
    else:
        return (num - 1) // 2 + num % 2

nim_s = 0
for num in arr:
    nim_s ^= get_grundy_num(num)
if nim_s == 0:
    print("cubelover")
else:
    print("koosaga")
