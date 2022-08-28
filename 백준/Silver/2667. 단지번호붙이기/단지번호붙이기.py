import sys

input = sys.stdin.readline

n = int(input())
arr = [[int(x) for x in input().strip()] for i in range(n)]

visited = [False] * (n * n)

c = 0

graph = [[] for i in range(n * n)]

for i in range(n):
    for j in range(n):


        if j != n - 1:

            if arr[i][j] == arr[i][j + 1] == 1:
                graph[i * n + j].append(i * n + j + 1)
                graph[i * n + j + 1].append(i * n + j)
        if i != n - 1:
            if arr[i][j] == arr[i + 1][j] == 1:
                graph[i * n + j].append((i + 1) * n + j)
                graph[(i + 1) * n + j].append(i * n + j)



def dfs(graph, s):
    result = []
    visited[s] = True
    result.append(s)

    for near_node in graph[s]:
        if visited[near_node] is False:
            result.extend(dfs(graph, near_node))
    return result

output = []

for i in range(n * n):
    if visited[i] is not True and arr[i // n][i % n] == 1:
        output.append(dfs(graph, i))

print(len(output))
output.sort(key=lambda x : len(x))
for lis in output:
    print(len(lis))


