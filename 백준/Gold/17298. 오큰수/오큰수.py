import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

stack = [0] * n
top = -1

result_arr = [-1] * n

lis = []

for i, num in enumerate(arr):

    if top != -1 and arr[stack[top]] < num:

        for j in range(top + 1):

            if arr[stack[top]] >= num:
                break

            result_arr[stack[top]] = num

            top -= 1

    top += 1
    stack[top] = i

print(*result_arr, sep=" ")
