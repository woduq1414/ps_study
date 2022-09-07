import sys
import math

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
abs_arr = [ abs(x) for x in arr]


result = []

left = 0
right = n - 1

while left != right:

    result.append([abs(arr[left] + arr[right]), [left, right]])

    if abs_arr[left] >= abs_arr[right]:
        left += 1
    else:
        right -= 1

result.sort(key = lambda x : x[0])

print(arr[result[0][1][0]], arr[result[0][1][1]], sep=" ")
