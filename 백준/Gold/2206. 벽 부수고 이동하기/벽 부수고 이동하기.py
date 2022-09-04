import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [
    [int(x) for x in input().strip()] for i in range(n)
]


def bfs(s):
    queue = deque()
    visited = [[[0] * 2 for i in range(m)] for j in range(n)]

    queue.append((s[0], s[1], 0))
    visited[s[0]][s[1]][0] = 1

    c = 0
    while queue:
        c += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            if node[0] == n - 1 and node[1] == m -1:
                return c



            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            for i in range(4):
                next_node = (node[0] + dx[i], node[1] + dy[i], node[2])

                if (0 <= next_node[0] < n) and (0 <= next_node[1] < m):
                    if arr[next_node[0]][next_node[1]] == 0:
                        if visited[next_node[0]][next_node[1]][next_node[2]] == 0:

                            queue.append(next_node)
                            visited[next_node[0]][next_node[1]][next_node[2]] = 1

                    else:

                        if next_node[2] == 0:
                            if visited[next_node[0]][next_node[1]][
                                next_node[2]] == 0:
                                queue.append((next_node[0], next_node[1], 1))
                                visited[next_node[0]][next_node[1]][
                                    1] = 1


                else:
                    continue



    return -1


print(bfs((0, 0)))
