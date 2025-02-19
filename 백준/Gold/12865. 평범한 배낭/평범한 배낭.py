import sys


def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())

dp = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())
    for j in reversed(range(0, k - w + 1, 1)):
        if j == 0 or dp[j] != 0:
            dp[j + w] = max(dp[j + w], dp[j] + v)

# print(dp)
print(max(dp))