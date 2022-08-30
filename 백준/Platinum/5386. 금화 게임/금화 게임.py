import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):

    s, k = map(int, input().split())
    if k % 2 == 1:
        if s % 2 == 1:
            print(1)
        else:
            print(0)
    else:
        t = s

        r = (s - 1) % (k + 1)
        if r % 2 == 0 and r != k:
            print(1)
            continue

        while s >= 0:
            r = s % (k + 1)
            if r % 2 == 0 and r != k:
                print(t-s)
                break
            else:
                s -= k
