import sys

input = sys.stdin.readline

n = int(input())
arr = [[x for x in input().strip()] for i in range(n)]


def func(s_x, s_y, length):
    if length == 1:
        return str(arr[s_y][s_x])

    a = func(s_x + 0, s_y + 0, length // 2)
    b = func(s_x + length // 2, s_y + 0, length // 2)
    c = func(s_x, s_y + length // 2, length // 2)
    d = func(s_x + length // 2, s_y + length // 2, length // 2)
    if len(a) == 1 and a == b == c == d:
        return a
    else:
        return f"({a}{b}{c}{d})"


print(func(0, 0, n))
