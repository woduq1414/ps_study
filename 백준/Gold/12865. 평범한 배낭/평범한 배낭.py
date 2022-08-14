import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

memo = [[0] * (k + 1) for i in range(n)]

if arr[0][0] <= k:
    memo[0][arr[0][0]] = arr[0][1]

for i in range(1, n):
    w, v = arr[i]

    if w > k:
        for j in range(1, k + 1):
            memo[i][j] = memo[i - 1][j]
    else:

        for j in range(1, k + 1):

            memo[i][j] = memo[i - 1][j]

            if j == w:
                memo[i][j] = max(memo[i][j], v)
            elif j > w:
                memo[i][j] = max(memo[i][j], memo[i - 1][j - w] + v)


print(max(max(memo[-1]), 0))
