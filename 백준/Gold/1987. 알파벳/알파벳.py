import sys

# sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    [ord(x) - 65 for x in input().strip()] for i in range(n)
]

max_result = 0

visited = [0] * 26


def dfs(x, y, c):
    global max_result

    ch = arr[y][x]
    max_result = max(max_result, c - 1)

    if x < m - 1:
        if not visited[ch]:
            visited[ch] = 1
            dfs(x + 1, y, c + 1)
            visited[ch] = 0
    if x > 0:
        if not visited[ch]:
            visited[ch] = 1
            dfs(x - 1, y, c + 1)
            visited[ch] = 0
    if y < n - 1:
        if not visited[ch]:
            visited[ch] = 1
            dfs(x, y + 1, c + 1)
            visited[ch] = 0
    if y > 0:
        if not visited[ch]:
            visited[ch] = 1
            dfs(x, y - 1, c + 1)
            visited[ch] = 0


dfs(0, 0, 1)

print(max_result)
