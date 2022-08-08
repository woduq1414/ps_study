import sys
import copy


input = sys.stdin.readline

n = int(input())

c = 0


def func(queens, line, nn):
    if line == nn:
        global c
        c += 1
        return

    for i in range(nn):

            flag = True
            for j, x in enumerate(queens):
                if x == i or x + j == i + line or x - j == i - line:
                    flag = False
                    break
            if flag is True:

                func(queens + [i], line + 1, nn)


queen_non = []
func(queen_non, 0, n)
print(c)
