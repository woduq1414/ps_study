import sys
import math

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n = int(input())

parents = [i for i in range(n + 1)]  # 먼저 모든 노드의 루트를 자신으로 지정한다.


def find(x):
    # if x == parents[x]:
    #     return x
    # else:
    #     y = find(parents[x])
    #     parents[x] = y
    #     return y
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:  # 합쳐준다.
        parents[y] = x
    else:
        return False
    return True


v_arr = []
e_arr = []


for i in range(n):
    a, b = map(float, input().split())
    for j, v in enumerate(v_arr):
        c, d = v
        e_arr.append([i, j, math.sqrt((c - a) ** 2 + (d - b) ** 2)])
    v_arr.append([a, b])


e_arr.sort(key = lambda x : x[2])

s = 0
t = []
for i in range(len(e_arr)):
    a, b, c = e_arr[i]

    if union(a,b):

        t.append(c)
        s += c

print(s)
