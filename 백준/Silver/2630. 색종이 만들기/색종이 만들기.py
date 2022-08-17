import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

cnt = 0


def func(s_x, s_y, length, f):
    global cnt

    if length == 1:
        return abs(f - arr[s_y][s_x])

    a = func(s_x + 0, s_y + 0, length // 2, f)
    b = func(s_x + length // 2, s_y + 0, length // 2, f)
    c = func(s_x, s_y + length // 2, length // 2, f)
    d = func(s_x + length // 2, s_y + length // 2, length // 2, f)
    if a and b and c and d:
        return True
    else:
        cnt += sum([a, b, c, d])
        return False


if func(0, 0, n, 1):
    cnt += 1
print(cnt)

cnt = 0
if func(0, 0, n, 0):
    cnt += 1

print(cnt)
