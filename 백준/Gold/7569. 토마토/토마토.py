import sys
from collections import deque
import copy

input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for i in range(n)] for j in range(h)]

arr_1 = []
cnt_not_tomato = 0

for i in range(n):
    for j in range(m):
        for k in range(h):
            if arr[k][i][j] == 1:
                arr_1.append((j, i, k))
            elif arr[k][i][j] == -1:
                cnt_not_tomato += 1

visited = {

}


def bfs(lis):
    queue = deque()

    for s in lis:
        queue.append(s)
        visited[s] = 0

    c = 0

    while queue:

        node = queue.popleft()

        c += 1

        dx = [1, 0, -1, 0, 0, 0]
        dy = [0, 1, 0, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        for i in range(6):

            near_node = (node[0] + dx[i], node[1] + dy[i], node[2] + dz[i])

            if near_node[0] < 0 or near_node[0] >= m or near_node[1] < 0 or \
                    near_node[1] >= n or near_node[2] < 0 or \
                    near_node[2] >= h:
                continue

            if arr[near_node[2]][near_node[1]][near_node[0]] == -1:
                continue

            # if near_node not in visited:
            if arr[near_node[2]][near_node[1]][near_node[0]] == 0:
                arr[near_node[2]][near_node[1]][near_node[0]] = 1
                visited[near_node] = min(visited[node] + 1,
                                         visited.get(near_node, 999999))
                queue.append(near_node)

    return visited


result = bfs(arr_1)

if len(result) == m * n * h - cnt_not_tomato:
    print(max(result.values()))
else:
    print(-1)
