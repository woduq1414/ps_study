import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lis = []

def func(nn, output, c):
    if c == 0:
        return

    for num in range(1, n+1):
        if len(output) > 0 and num < output[-1]:
            continue
        output_new = output[:]

        output_new.append(num)
        if c == 1:

            r = [arr[num - 1] for num in output_new]
            if r not in lis:
                lis.append(r)


        func(nn, output_new, c - 1)


func(n, [], m)

for l in lis:
    print(*l)