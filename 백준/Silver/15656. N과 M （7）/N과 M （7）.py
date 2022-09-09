import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def func(nn, output, c):
    if c == 0:
        return

    for num in range(1, n+1):

        output_new = output[:]

        output_new.append(arr[num - 1])
        if c == 1:

            print(*output_new)



        func(nn, output_new, c - 1)


func(n, [], m)
