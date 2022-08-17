import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

cnt_lis = [0, 0, 0]


def func(s_x, s_y, length):

    if length == 1:
        return arr[s_y][s_x]

    ar = []

    for i in range(3):
        for j in range(3):
            ar.append(
                func(s_x + length // 3 * j, s_y + length // 3 * i, length // 3))

    f = True
    for i in range(8):
        if ar[i] is not None and ar[i] == ar[i + 1]:
            pass
        else:
            f = False
            break

    if f:

        return ar[0]

    else:
        for i in range(9):
            if ar[i] is not None:
                cnt_lis[ar[i] + 1] += 1

        return None

result = func(0, 0, n)
if result is not None:
    cnt_lis[result + 1] += 1
print(*cnt_lis, sep="\n")
