import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def bfs(s):
    visited = [0] * 1000001
    queue = deque()

    queue.append([s])



    while queue:

        node = queue.popleft()
        node_last = node[-1]
        if node_last == 1:
            return visited[1], node


        a, b = divmod(node_last, 2)
        c, d = divmod(node_last, 3)

        near_node_list = [node_last - 1]
        if b == 0 :
            near_node_list.append(a)
        if d == 0 :
            near_node_list.append(c)


        for near_node in near_node_list:

            if visited[near_node] == 0:
                visited[near_node] = visited[node_last] + 1
                queue.append(node + [near_node])


c, lis = bfs(n)
print(c)
print(*lis, sep=" ")