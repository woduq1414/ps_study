import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
dist = [float('inf')] * (v + 1)
dist[s] = 0

graph = [[] for i in range(v + 1)]
for i in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

heap = []
heapq.heappush(heap, (0, s))

while heap:

    d, node = heapq.heappop(heap)

    if dist[node] < d:
        continue

    for next_node, next_d in graph[node]:
        update_d = d + next_d
        if dist[next_node] > update_d:
            dist[next_node] = update_d
            heapq.heappush(heap, (update_d, next_node))

for d in dist[1: v + 1]:
    if d == float("inf"):
        print("INF")
    else:
        print(d)
