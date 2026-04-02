import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))


dp = [0] * n

if n == 1:
    print(lis[0])
    exit()
elif n == 2:
    print(lis[0] + lis[1])
    exit()


dp[0] = lis[0]
dp[1] = lis[0] + lis[1]




dp[2] = max(lis[0] + lis[2], lis[1] + lis[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + lis[i - 1], dp[i- 2]) + lis[i]

# print(dp)
print(dp[n-1])