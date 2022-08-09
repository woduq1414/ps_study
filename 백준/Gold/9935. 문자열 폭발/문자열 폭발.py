import sys

input = sys.stdin.readline

s = input().strip("\n")
ex = input().strip("\n")
exlen = len(ex)

stack = [None] * len(s)
p = 0


def isTopEx():
    for i in range(0, exlen):

        if stack[p - i] != ex[-(i + 1)]:
            return False
    return True


for c in s:

    stack[p] = c
    while p >= exlen - 1 and isTopEx():
        p -= exlen
    p += 1

if p == 0:
    print("FRULA")
else:
    print(*stack[:p], sep="")
