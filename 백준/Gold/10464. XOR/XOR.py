import sys
import math

input = sys.stdin.readline

n = int(input())

result = 0

for i in range(n):
    nim_s = 0

    x , y = map(int, input().split())

    m = y - x + 1

    if x % 2 == 0:
        r = m % 4
        if  r == 0:
            nim_s = 0
        elif r == 1:
            nim_s = x + m - 1
        elif r == 2:
            nim_s = 1
        else:
            nim_s = 1 ^ (x + m - 1)
    else:
        r = m % 4
        if r == 0:
            nim_s = x ^ (x + m - 1) ^ 1
        elif r == 1:
            nim_s = x
        elif r == 2:
            nim_s = x ^ (x + m - 1)
        else:
            nim_s = x ^ 1

    print(nim_s)
