import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

s = set()

def func(lis, output, c):
    if c == 0:
        return


    for num in lis:

        if len(output) > 0 and num < output[-1]:
            continue

        temp = lis[:]
        output_new = output[:]

        output_new.append(num)
        if c == 1:

            s.add(tuple(output_new))

        temp.remove(num)

        func(temp, output_new, c - 1)


func(arr, [], m)

result = sorted(list(s))
for r in result:
    print(*r, sep = " ")