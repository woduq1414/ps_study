import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

stack = [0] * n
top = -1

result_arr = [-1] * n

lis = []


cnt_arr = [0] * 1000001
for num in arr:
    cnt_arr[num] += 1

freq_arr = [0] * n
for i, num in enumerate(arr):
    freq_arr[i] = cnt_arr[num]



for i, num in enumerate(freq_arr):

    if top != -1 and freq_arr[stack[top]] < num:

        for j in range(top + 1):

            if freq_arr[stack[top]] >= num:
                break

            result_arr[stack[top]] = i

            top -= 1

    top += 1
    stack[top] = i


print(*[arr[x] if x != -1 else -1 for x in result_arr], sep=" ")
