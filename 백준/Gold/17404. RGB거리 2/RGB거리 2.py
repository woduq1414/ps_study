import sys
import copy
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n) ]
arr_t = copy.deepcopy(arr)


lis = []

for k in range(3):

    line = [9999, 9999, 9999]
    line[k] = arr[0][k]


    for i in range(1, n ):

        new_line = arr[i][:]
        if i == n - 1:
            new_line[k] = 9999


        new_line[0] += min(line[1], line[2])
        new_line[1] += min(line[0], line[2])
        new_line[2] += min(line[0], line[1])

        line = new_line



    lis.append(min(line))

    arr = arr_t


print(min(lis))
