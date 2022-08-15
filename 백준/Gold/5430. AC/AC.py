import sys

from collections import deque

input = sys.stdin.readline

T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    arr = deque(eval(input()))

    f = True
    is_error = False

    for func in p:
        if func == "R":
            f = not f
        elif func == "D":

            if len(arr) == 0:
                is_error = True
                break

            if f is True:
                arr.popleft()
            else:
                arr.pop()

    if is_error is False:

        if f is False:
            arr.reverse()

        print("[", end="")
        print(*arr, sep=",", end="]\n")
    else:
        print("error")
