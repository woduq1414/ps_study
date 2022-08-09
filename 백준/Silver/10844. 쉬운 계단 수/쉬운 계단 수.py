import sys

input = sys.stdin.readline

n = int(input())

arr = [0,1,1,1,1,1,1,1,1,1]

for i in range(n-1):
    new_arr = [0] * 10
    for idx, c in enumerate(arr):
        if idx == 0:
            new_arr[1] += c
        elif idx == 9:
            new_arr[8] += c
        else:
            new_arr[idx - 1] += c
            new_arr[idx + 1] += c

    arr = new_arr

print(sum(arr) % 1000000000)