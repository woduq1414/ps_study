import sys
from collections import deque
# https://www.acmicpc.net/problem/17071
input = sys.stdin.readline

n, k = map(int, input().split())




def bfs(s):
    global k
    visited = [0] * 500001

    visited2 = [[0] * 500001, [0] * 500001]

    queue = deque()

    queue.append(s)
    depth = 1
    visited2[0][s] = 1

    while queue:
        k += depth

        # print(depth)

        if  k > 500000:
            return -1

        if visited2[(depth) % 2][k] == 1:

            return depth
        queue_len = len(queue)
        for i in range(queue_len):



            node = queue.popleft()


            for near_node in [node - 1, node + 1, node * 2]:


                if k == near_node:
                    return depth

                if near_node < 0 or near_node > 500000:
                    continue

                # print(near_node, k)


                if visited2[depth % 2][near_node] == 1:
                    continue


                queue.append(near_node)
                visited2[depth % 2][near_node] = 1


                # print(near_node, depth)



        depth += 1


                    # queue.append(near_node)
if n == k:
    print(0)
else:
    print(bfs(n))