import sys

import heapq



input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ [] for i in range(n + 1) ]
degree = [ 0 for i in range(n + 1) ]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1


queue = []


result = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    node = heapq.heappop(queue)
    result.append(node)

    for near_node in graph[node]:

        degree[near_node] -= 1
        if degree[near_node] == 0:
            heapq.heappush(queue, near_node)


print(*result, sep = " ")