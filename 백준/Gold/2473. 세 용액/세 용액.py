import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

result = []

lis = []

min_sum = float('inf')
min_lis = []

for i in range(n - 2):

    t = arr[i]
    del arr[i]
    abs_arr = [abs(x + t) for x in arr]

    left = 0
    right = n - 2

    while left != right:

        s = arr[left] + arr[right] + t
        if min_sum > abs(s):
            min_sum = abs(s)
            min_lis = [t, arr[left], arr[right]]

        if min_sum > s:
            left += 1
        else:
            right -= 1


        if min_sum == 0:
            break
    if min_sum == 0:
        break
    arr.insert(i, t)

print(*sorted(min_lis), sep=" ")
