import sys

from collections import defaultdict

input = sys.stdin.readline

n = int(input())
min_k = 10

graph = defaultdict(set)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].add(i + 1)
    graph[b].add(i + 1)
# print(graph)

isolated_cnt = 0

for x in graph:
    if len(graph[x]) == 0:
        isolated_cnt += 1


result = [[1]]

for i in range(100):
    prev = result[i]
    r = set([])

    for node in prev:
        for x in graph[node]:
            r.add(x)

    result.append(r)

# print(result, isolated_cnt)


if len(result[min_k]) >= n - isolated_cnt:
    print(-1)
else:
    for x in range(min_k,len(result)):

        if 1 not in result[x]:
            print(x)
            exit()

    print(-1)

