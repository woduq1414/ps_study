import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

tunnel = {}
for i in range(n + m):
    x, y = map(int, input().split())
    tunnel[x] = y


def bfs(s):

    queue = deque()
    visited = [0] * 101

    queue.append(s)
    visited[s] = 1

    c = 0
    while queue:
        c += 1

        for _ in range(len(queue)):
            node = queue.popleft()

            for i in range(1, 7):
                next_node = node + i
                if next_node in tunnel:
                    next_node = tunnel[next_node]

                if next_node >= 100:
                    return c


                if visited[next_node] == 0:

                    queue.append(next_node)
                    visited[next_node] = 1


    return c


print(bfs(1))


