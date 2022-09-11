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
    a, b, c = map(int, input().split())
    v_arr.append([i, a, b, c])

for i in range(3):

    v_arr.sort(key=lambda x: x[i + 1])

    for j in range(len(v_arr) - 1):
        e_arr.append([v_arr[j][0],
                      v_arr[j + 1][0],
                      abs(v_arr[j][i + 1] - v_arr[j + 1][i + 1])])

e_arr.sort(key=lambda x: x[2])

s = 0

for i in range(len(e_arr)):
    a, b, c = e_arr[i]

    if union(a, b):
        s += c


print(s)
