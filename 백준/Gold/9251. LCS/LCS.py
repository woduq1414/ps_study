import sys
from collections import defaultdict

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
# print(len(s1) + len(s2))

dp[0][0] = 0
for i in range(1, len(s1) + len(s2) + 1):
    for j in range(0, i + 1):
        k = i - j
        # print(i, j, k)

        if j > len(s1) or k > len(s2):
            continue

        if j == 0 or k == 0:
            dp[j][k] = 0
        elif s1[j - 1] == s2[k - 1]:
            dp[j][k] = dp[j - 1][k - 1] + 1
        else:
            dp[j][k] = max(dp[j - 1][k], dp[j][k - 1])

print(dp[len(s1)][len(s2)])
