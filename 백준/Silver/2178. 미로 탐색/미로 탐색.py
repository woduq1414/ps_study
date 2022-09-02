import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[int(x) for x in input().strip()] for i in range(n)]

visited = [False] * (m * n)

c = 0

graph = [[] for i in range(m * n)]

for i in range(n):
    for j in range(m):

        if j != m - 1:

            if arr[i][j] == arr[i][j + 1] == 1:
                graph[i * m + j].append(i * m + j + 1)
                graph[i * m + j + 1].append(i * m + j)
        if i != n - 1:
            if arr[i][j] == arr[i + 1][j] == 1:
                graph[i * m + j].append((i + 1) * m + j)
                graph[(i + 1) * m + j].append(i * m + j)


def bfs(graph, s):
    result = []

    visited = [False for i in range(m * n + 1)]
    queue = deque()

    queue.append(s)
    visited[s] = True
    result.append(s)

    c = 2
    while queue:

        for i in range(len(queue)):
            node = queue[i]
            for near_node in graph[node]:
                if visited[near_node] is False:
                    result.append(near_node)


                    visited[near_node] = True
                    queue.append(near_node)

                    if near_node == m * n - 1:
                        return c
        c += 1

    return c


output = []


print(bfs(graph, 0))

# print(dfs(graph, 0).index(n * m - 1))