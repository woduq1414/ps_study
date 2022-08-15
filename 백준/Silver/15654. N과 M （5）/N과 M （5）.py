import sys
import copy


input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def func(lis, output, c):
    if c == 0:
        return

    for num in lis:
        temp = copy.deepcopy(lis)
        output_new = copy.deepcopy(output)

        output_new.append(num)
        if c == 1:
            print(*output_new)

        temp.remove(num)

        func(temp, output_new, c - 1)


func(arr, [], m)