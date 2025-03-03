import sys

# sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [0] * (k + 1)
dp[0] = 1
for c in arr:
    for i in range(c, k + 1):

        dp[i] += dp[i - c]

print(dp[-1])