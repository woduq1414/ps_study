import heapq
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    v, e, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for i in range(2001)]

    dd = None

    for i in range(e):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))

        if (a == g and b == h) or (a == h and b == g):
            dd = w

    dest_arr = [int(input()) for i in range(t)]


    def get_dist(graph, s):

        distance = [int(1e10)] * 2001  # 처음 거리는 모두 무한대로 초기화
        distance[s] = 0

        pq = []
        heapq.heappush(pq, (0, s))
        while pq:
            currCost, currPos = heapq.heappop(pq)
            if currCost > distance[currPos]:
                continue

            for nextCost, nextPos in graph[currPos]:
                if currCost + nextCost < distance[nextPos]:
                    distance[nextPos] = currCost + nextCost
                    heapq.heappush(pq, (currCost + nextCost, nextPos))

        # print(distance)
        return distance


    result = []

    dist_s = get_dist(graph, s)
    dist_g = get_dist(graph, g)
    dist_h = get_dist(graph, h)

    for i in range(t):
        d = dest_arr[i]

        if dist_s[d] == dd + min(dist_s[g] + dist_h[d], dist_s[h] + dist_g[d]):
            result.append(d)
    result.sort()
    print(*result, sep=" ")
