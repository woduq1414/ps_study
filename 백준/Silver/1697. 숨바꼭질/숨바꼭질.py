import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())


def bfs(s):
    visited = [0] * 100001
    queue = deque()

    queue.append(s)

    while queue:

        node = queue.popleft()

        if node == k:
            return visited[k]

        for near_node in [node - 1, node + 1, node * 2]:

            if near_node < 0 or near_node > 100000:
                continue

            if visited[near_node] == 0:
                visited[near_node] = visited[node] + 1
                queue.append(near_node)


print(bfs(n))
