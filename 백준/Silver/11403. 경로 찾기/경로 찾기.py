import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = {}

for i in range(n):
    line_arr = list(map(int, input().split()))
    graph[i] = []
    for j in range(n):
        if line_arr[j]:
            graph[i].append(j)

result = [[0] * n for _ in range(n)]

for k in range(n):
    visited = [False] * n   # 시작점마다 초기화
    stack = [k]

    while stack:
        node = stack.pop()

        for near_node in graph[node]:
            if not visited[near_node]:
                visited[near_node] = True
                result[k][near_node] = 1
                stack.append(near_node)

for i in range(n):
    print(*result[i])