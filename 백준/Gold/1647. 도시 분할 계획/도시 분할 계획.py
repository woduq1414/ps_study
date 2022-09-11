import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

v, e = map(int, input().split())

parents = [i for i in range(v + 1)]  # 먼저 모든 노드의 루트를 자신으로 지정한다.


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

arr = []


for i in range(e):
    a, b,c  = map(int, input().split())

    arr.append([a,b,c])

arr.sort(key = lambda x : x[2])

s = 0
t = []
for i in range(e):
    a, b, c = arr[i]

    if find(a) != find(b):
        union(a, b)
        t.append(c)
        s += c

print(s - max(t))
