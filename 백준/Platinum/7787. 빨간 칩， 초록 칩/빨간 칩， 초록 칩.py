import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

r, g = map(int, input().split())

c1 = 1
while r > 0:
    if r % 2 == 0:
        r //= 2
        c1 += 1
    else:
        break

c2 = 1
while g > 0:
    if g % 2 == 0:
        g //= 2
        c2 += 1
    else:
        break

nim_s = c1 ^ c2

if nim_s == 0:
    print("B player wins")
else:
    print("A player wins")