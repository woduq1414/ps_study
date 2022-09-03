import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
name = input().strip()


nim_s = 0
for num in arr:
    nim_s ^= num - 2


print(["Whiteking", "Blackking"][(name == "Blackking") ^ (nim_s == 0)])
