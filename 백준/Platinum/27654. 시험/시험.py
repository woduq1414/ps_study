import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, k = map(int, input().split())
data = []
for i in range(n):
    p, q = map(int, input().split())
    data.append([p, q])


def check(D):
    y_list = []
    for x in data:
        y_list.append(-x[1] * D + x[0])

    y_list.sort(reverse=True)
    return sum(y_list[:k]) >= 0


def parametric_search(l, r, f):
    eps = 1e-9  
    while r - l > eps:
        mid = (l + r) / 2
        if f(mid):
            l = mid
        else:
            r = mid

    return l


print(parametric_search(0, 1, check))
