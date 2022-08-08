import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
op = tuple(map(int, input().split()))

min_num, max_num = 10 ** 10, - 10 ** 10


def func(lis, output, c, limit):
    global nums
    if limit == 0:

        global max_num, min_num
        if output > max_num:
            max_num = output
        if output < min_num:
            min_num = output

        return

    if lis[0] >= 1:
        tmp = output + nums[c + 1]
        func((lis[0] - 1, lis[1], lis[2], lis[3]), tmp, c + 1, limit - 1)
        # print("+", end="->")
    if lis[1] >= 1:
        tmp = output - nums[c + 1]
        func((lis[0], lis[1] - 1, lis[2], lis[3]), tmp, c + 1, limit - 1)
    if lis[2] >= 1:
        tmp = output * nums[c + 1]
        func((lis[0], lis[1], lis[2] - 1, lis[3]), tmp, c + 1, limit - 1)
    if lis[3] >= 1:
        if output < 0:
            tmp = -(abs(-output // nums[c + 1]))
        else:
            tmp = output // nums[c + 1]
        func((lis[0], lis[1], lis[2], lis[3] - 1), tmp, c + 1, limit - 1)


func(op, nums[0], 0, n - 1)
print(max_num)
print(min_num)
