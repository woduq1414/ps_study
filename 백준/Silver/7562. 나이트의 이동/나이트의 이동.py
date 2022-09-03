import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())


    def bfs(s):
        visited = {

        }
        queue = deque()

        queue.append(s)
        visited[s] = 0

        while queue:

            node = queue.popleft()

            if node == (ex, ey):
                return visited[node]

            dx = [1, 2, 2, 1, -1, -2, -2, -1]
            dy = [2, 1, -1, -2, -2, -1, 1, 2]

            for i in range(8):

                near_node = (node[0] + dx[i], node[1] + dy[i])

                if near_node[0] < 0 or near_node[0] >= l or near_node[1] < 0 or \
                        near_node[1] >= l:
                    continue

                if near_node not in visited:
                    visited[near_node] = visited[node] + 1
                    queue.append(near_node)


    print(bfs((sx, sy)))
