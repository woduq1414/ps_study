import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())

    arr = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1


    visited = [False] * (m * n)

    c = 0

    graph = [[] for i in range(m * n)]

    for i in range(n):
        for j in range(m):


            if j != m - 1:

                if arr[i][j] == arr[i][j + 1] == 1:
                    graph[i * m + j].append(i * m + j + 1)
                    graph[i * m + j + 1].append(i * m + j)
            if i != n - 1:
                if arr[i][j] == arr[i + 1][j] == 1:
                    graph[i * m + j].append((i + 1) * m + j)
                    graph[(i + 1) * m + j].append(i * m + j)



    def dfs(graph, s):
        result = []
        visited[s] = True
        result.append(s)

        for near_node in graph[s]:
            if visited[near_node] is False:
                result.extend(dfs(graph, near_node))
        return result

    output = []

    for i in range(m * n):
        if visited[i] is not True and arr[i // m][i % m] == 1:
            output.append(dfs(graph, i))


    print(len(output))



