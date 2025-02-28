import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
min_time = -1

def bfs(s):
    visited = [0] * 100001
    queue = deque()

    queue.append(s)

    while queue:

        node = queue.popleft()
        # print(node)
        if node == k:
            global min_time, cnt
            if min_time == -1:
                min_time = visited[k]

            else:
                if visited[k] == min_time:
                    pass
                elif visited[k] > min_time:
                    return (min_time, cnt)
            cnt += 1
            # print(visited[k], cnt, min_time, k)


            # return visited[k]

        for near_node in [node - 1, node + 1, node * 2]:

            if near_node < 0 or near_node > 100000:
                continue

            if visited[near_node] == 0:


                visited[near_node] = visited[node] + 1
                # print(node, near_node)
                queue.append(near_node)
            else:
                # visited[near_node] = min(visited[node] + 1, visited[near_node])
                # print(node, near_node)

                if visited[near_node] == visited[node] + 1:
                    queue.append(near_node)
                elif visited[near_node] > visited[node] + 1:
                    visited[near_node] = visited[node] + 1
                    queue.append(near_node)
                else:
                    pass


                if min_time != -1 and visited[near_node] > min_time + 1:
                    return (min_time, cnt)
                # queue.append(near_node)
    return (min_time, cnt)
print(*bfs(n), sep='\n')