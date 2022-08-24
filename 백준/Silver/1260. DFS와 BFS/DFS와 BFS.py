import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    graph[i].sort()


def dfs(graph, s):
    global result

    visited[s] = True
    result.append(s)

    for near_node in graph[s]:
        if visited[near_node] is False:
            dfs(graph, near_node)


def bfs(graph, s):
    global result

    visited = [False for i in range(n + 1)]
    queue = deque()

    queue.append(s)
    visited[s] = True
    result.append(s)


    while queue:
        node = queue.popleft()

        for near_node in graph[node]:
            if visited[near_node] is False:
                result.append(near_node)


                visited[near_node] = True
                queue.append(near_node)

    return visited


result = []

visited = [False for i in range(n + 1)]

dfs(graph, r)

print(*result, sep=" ")

result = []


bfs(graph, r)
print(*result, sep=" ")
