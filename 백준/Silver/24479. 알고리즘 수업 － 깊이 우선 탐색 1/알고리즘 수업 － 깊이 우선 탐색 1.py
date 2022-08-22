import sys
sys.setrecursionlimit(10**8)


input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    graph[i].sort()

result = [0] * (n + 1)
c = 1
visited = [False for i in range(n + 1)]


def dfs(graph, s):
    global result, c

    visited[s] = True
    result[s] = c
    c += 1

    for near_node in graph[s]:
        if visited[near_node] is False:
            dfs(graph, near_node)


dfs(graph, r)

for node in result[1:]:
    print(node)
