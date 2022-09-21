import sys

input = sys.stdin.readline

m, n = int(input()), int(input())


def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr


lis = is_prime_num(n)
s = 0
mi = -1
for i in range(n, m - 1, -1):
    if lis[i] is True:
        s += i
        mi = i
if s == 0:
    print(-1)
else:
    print(s)
    print(mi)
