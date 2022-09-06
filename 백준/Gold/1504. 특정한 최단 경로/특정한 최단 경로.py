import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())



graph = [[] for i in range(v + 1)]
for i in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

v1,v2 = map(int, input().split())


def get_dist(graph, s):

    dist = [float('inf')] * (v + 1)
    dist[s] = 0


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

    return dist

dist_1 = get_dist(graph, 1)
s_v1 = dist_1[v1]
s_v2 = dist_1[v2]

dist_v1 = get_dist(graph, v1)
v1_v2 = dist_v1[v2]
v1_n = dist_v1[v]

dist_v2 = get_dist(graph, v2)
v2_n = dist_v2[v]

result_1 = s_v1 + v1_v2 + v2_n
result_2 = s_v2 + v1_v2 + v1_n

if result_1 == float('inf') and result_2 == float('inf'):
    print(-1)
else:
    print(min(result_1, result_2))

