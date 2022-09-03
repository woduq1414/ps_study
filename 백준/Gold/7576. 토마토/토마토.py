import sys
from collections import deque
import copy

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

arr_1 = []
cnt_not_tomato = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr_1.append((j, i))
        elif arr[i][j] == -1:
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

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):

            near_node = (node[0] + dx[i], node[1] + dy[i])

            if near_node[0] < 0 or near_node[0] >= m or near_node[1] < 0 or \
                    near_node[1] >= n:
                continue

            if arr[near_node[1]][near_node[0]] == -1:
                continue

            # if near_node not in visited:
            if arr[near_node[1]][near_node[0]] == 0:
                arr[near_node[1]][near_node[0]] = 1
                visited[near_node] = min(visited[node] + 1, visited.get(near_node, 999999))
                queue.append(near_node)


    return visited


result = None



result = bfs(arr_1)

if len(result) == m * n - cnt_not_tomato:
    print(max(result.values()))
else:
    print(-1)
