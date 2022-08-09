import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_sum_value = - 10 ** 10
max_negative_value = - 10000

s = 0
is_all_negative = True

for num in arr:
    if num >= 0:
        is_all_negative = False
        s += num
    else:
        if max_sum_value < s:
            max_sum_value = s

        if s + num < 0:

            s = 0
        else:

            s += num

        if max_negative_value < num:
            max_negative_value = num

if max_sum_value < s:
    max_sum_value = s


if is_all_negative:
    print(max_negative_value)
else:
    print(max_sum_value)
