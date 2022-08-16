import sys

# sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())

    arr = [list(map(int, input().split())) for i in range(2)]
    dp = [[0] * n for i in range(2)]

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    if n > 1:

        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

        for j in range(2, n, 1):
            dp[0][j] = arr[0][j] + max(dp[1][j - 1], dp[1][j - 2])

            dp[1][j] = arr[1][j] + max(dp[0][j - 1], dp[0][j - 2])

    print(max(dp[0][-1], dp[1][-1]))
