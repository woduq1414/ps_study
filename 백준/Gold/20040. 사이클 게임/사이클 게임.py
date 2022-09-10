import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]  # 먼저 모든 노드의 루트를 자신으로 지정한다.


def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:  # 합쳐준다.
        parents[y] = x


for i in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(i + 1)
        exit()
    union(a, b)
print(0)
