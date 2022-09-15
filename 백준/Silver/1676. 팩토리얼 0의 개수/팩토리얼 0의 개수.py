import sys

input = sys.stdin.readline

n = int(input())

c_2 = 0
t = 2

while t <= n:
    c_2 += n // t
    t *= 2

c_5 = 0
t = 5

while t <= n:
    c_5 += n // t
    t *= 5

print(min(c_2, c_5))
