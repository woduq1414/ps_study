import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def func(lis, output, c):
    if c == 0:
        return

    for num in lis:



        temp = lis[:]
        output_new = output[:]

        output_new.append(num)
        if c == 1:

            print(*output_new)



        func(temp, output_new, c - 1)


func(list(range(1, n + 1)), [], m)
