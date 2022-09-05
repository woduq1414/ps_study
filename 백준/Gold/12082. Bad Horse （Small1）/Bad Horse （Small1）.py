import sys
from collections import deque, defaultdict

input = sys.stdin.readline

k = int(input())
for kk in range(k):

    # v, e = map(int, input().split())
    v = int(input())
    e = v

    visited = {}


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


    graph = defaultdict(list)

    edge_list = []

    for i in range(e):
        # x, y = map(int, input().split())
        x, y = input().split()

        edge_list.append([x, y])

        graph[x].append(y)
        graph[y].append(x)

        visited[x] = -1
        visited[y] = -1

    f = True
    for i in visited.keys():
        if visited[i] == -1:

            if bfs(i, 0) is False:
                f = False

    if f is True:
        print(f"Case #{kk + 1}: Yes")
    else:
        print(f"Case #{kk + 1}: No")
