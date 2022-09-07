import sys
import math

input = sys.stdin.readline

dp = [1, 2, 3]
for i in range(63):
    dp.append(dp[-1] + dp[-2])


def get_cnt_to_num(num):
    if num == 0:
        return 0

    t = num

    arr = []
    result = 0
    while num >= 1:
        if num % 2 == 0:
            num //= 2
            arr.append(0)
        else:
            num //= 2
            arr.append(1)

    l2 = int(math.log2(t))

    arr.reverse()

    f = False
    is_prev_1 = False
    switch = -1

    for i, v in enumerate(arr):

        if i == 0:
            result += dp[l2 - i]
            # print(t, l2 - i, "@@1")
            is_prev_1 = True
            continue


        if v == 1:
            if is_prev_1 is True:
                if switch == -1:
                    switch = 0
            if switch == -1:
                if is_prev_1 is False:
                    result += dp[l2 - i]

                    # print(t, l2 - i, "@@4")
            elif switch == 0:
                switch = 1
            elif switch == 1:
                result += dp[l2 - i]

                # print(t, l2- i, "@@2")

                switch = 0

            is_prev_1 = True
        else:
            if switch == 0:
                switch = 1
            elif switch == 1:
                result += dp[l2 - i]
                # print(t, l2 - i, "@@3")

                switch = 0
            is_prev_1 = False


    return t - result


n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    print(get_cnt_to_num(r) - get_cnt_to_num(l - 1))
#

# print(dp)
# c = 0
# for i in range(1, 1001):
#     r = i ^ (i * 2) ^ (i * 3)
#     if r == 0:
#         c += 1
#     if c != (i - get_cnt_to_num(i)):
#         print(i, "!!!!!!!!!!!!!!!!!!")
#
#     print(i, int(math.log2(i)), i - 2 ** int(math.log2(i)), c,
#           i - get_cnt_to_num(i))
