import sys
import heapq
from collections import deque, defaultdict

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i, g in enumerate(graph):
    graph[i].sort(reverse=True)

result = [0] * (n + 1)
c = 1


def bfs(graph, s):
    global result, c

    visited = [False for i in range(n + 1)]
    queue = deque()

    queue.append(s)
    visited[s] = True
    result[s] = c
    c += 1

    while queue:
        node = queue.popleft()

        for near_node in graph[node]:
            if visited[near_node] is False:

                result[near_node] = c
                c+=1


                visited[near_node] = True
                queue.append(near_node)

    return visited

bfs(graph, r)

for node in result[1:]:
    print(node)
