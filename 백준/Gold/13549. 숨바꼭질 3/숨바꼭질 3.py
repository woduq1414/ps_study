import sys
import math

# sys.setrecursionlimit(10 ** 8)


input = sys.stdin.readline

n, k = map(int, input().split())

if k <= n:
    print(n - k)
    exit()
f = False
if n == 0:
    f = True
    n += 1

log = math.log2(k / n)
if (int_log := int(log)) == log:
    if f is True:
        print(1)
    else:
        print(0)
else:

    c_lis = []

    for i in range(int_log - 3, int_log + 5, 1):

        if i < 0:
            continue

        remain = abs(int(k - n * math.pow(2, i)))

        c = 0

        for j in range(i, -1, -1):
            divisor = int(math.pow(2, j))

            if remain % divisor >= divisor / 2 + 1 and abs(
                    divisor - remain % divisor) < remain % (divisor / 2):
                c += remain // divisor + 1
                remain = abs(divisor - remain % divisor)
            else:
                c += remain // divisor
                remain = remain % divisor

            if remain == 0:
                break

        c_lis.append(c)

    if f is True:

        print(min(c_lis) + 1)
    else:
        print(min(c_lis))
