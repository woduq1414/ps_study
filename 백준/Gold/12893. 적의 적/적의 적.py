import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())

visited = [-1] * (v + 1)


def bfs(s, t1):
    queue = deque()
    queue.append((s, t1))

    visited[s] = t1

    while queue:
        node, t = queue.popleft()

        for near_node in graph[node]:
            if visited[near_node] == -1:
                visited[near_node] = 1 - t
                queue.append((near_node, 1 - t))
            elif visited[node] == visited[near_node]:
                return False

    return True


graph = [[] for i in range(v + 1)]

edge_list = []

for i in range(e):
    x, y = map(int, input().split())

    edge_list.append([x, y])

    graph[x].append(y)
    graph[y].append(x)

f = True
for i in range(1, v + 1):
    if visited[i] == -1:

        if bfs(i, 0) is False:
            f = False

if f is True:
    print(1)
else:
    print(0)
