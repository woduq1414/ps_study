import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [
    [int(x) for x in input().strip()] for i in range(n)
]


def bfs(s):
    queue = deque()
    visited = [[[0] * (k + 1) for i in range(m)] for j in range(n)]

    queue.append((s[0], s[1], 0))
    visited[s[0]][s[1]][0] = 1

    c = 0
    while queue:

        c += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            if node[0] == n - 1 and node[1] == m - 1:
                return c

            def do():

                y, x, r = next_node

                if arr[y][x] == 0:
                    if visited[y][x][
                        r] == 0:
                        queue.append(next_node)
                        visited[y][x][
                            r] = 1

                else:

                    if r < k:
                        if visited[y][x][
                            r + 1] == 0:
                            queue.append(
                                (y, x,
                                 r + 1))
                            visited[y][x][
                                r + 1] = 1

            if node[1] + 1 < m:
                next_node = (node[0], node[1] + 1, node[2])
                do()
            if node[1] - 1 >= 0:
                next_node = (node[0], node[1] - 1, node[2])
                do()
            if node[0] + 1 < n:
                next_node = (node[0] + 1, node[1], node[2])
                do()
            if node[0] - 1 >= 0:
                next_node = (node[0] - 1, node[1], node[2])
                do()

    return -1


print(bfs((0, 0)))
