import math
import sys
from itertools import combinations

input = sys.stdin.readline

a, b = map(int, input().split())

c_lis = []


def func(n, h):
    if n > b:
        return
    elif n == b:
        c_lis.append(h)
        return

    func(n * 2, h + 1)
    func(n * 10 + 1, h + 1)


func(a, 1)
if c_lis:
    print(min(c_lis))
else:
    print(-1)
