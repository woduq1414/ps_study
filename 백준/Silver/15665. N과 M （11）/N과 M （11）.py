import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = set()

def func(nn, output, c):
    if c == 0:
        return

    for num in range(1, n+1):

        output_new = output[:]

        output_new.append(arr[num - 1])
        if c == 1:

            s.add(tuple(output_new))



        func(nn, output_new, c - 1)


func(n, [], m)

s = sorted(list(s))
for e in s:
    print(*e, sep= " ")
