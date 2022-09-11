import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ [] for i in range(n + 1) ]
degree = [ 0 for i in range(n + 1) ]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1


queue = deque()


result = []
for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)

    for near_node in graph[node]:

        degree[near_node] -= 1
        if degree[near_node] == 0:
            queue.append(near_node)


print(*result, sep = " ")