import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

i = 2


memo = {}

def get_grundy_num(num):


    if num in memo:
        return memo[num], []



    i = 2

    s_num = None

    arr_list = []
    k_list = []


    while i <= num:

        f = False
        if i % 2 == 0:
            if num * 2 % i == 0 and num % i != 0:
                s_num = num // i - (i - 2) // 2
                f = True
        else:
            if num % i == 0:
                s_num = num // i - (i - 1) // 2
                f = True

        if f is True:
            if s_num <= 0:
                break
            else:
                new_arr = [s_num + j for j in range(i)]
                # print(new_arr)
                arr_list.append(new_arr)
                k_list.append(i)
            # print(i)
        i += 1

    if len(arr_list) == 0:
        # print(num, ":", 0)

        memo[num] = 0

        return 0, []
    else:
        grundy_arr = [0] * 1000001

        nim_s_0_lis = []

        for arr in arr_list:
            nim_s = 0
            for nn in arr:
                nim_s ^= get_grundy_num(nn)[0]
            grundy_arr[nim_s] = 1

            if nim_s == 0:
                nim_s_0_lis.append(len(arr))

        # print(grundy_arr[:18])

        grundy_num = 0
        while grundy_arr[grundy_num] == 1:
            grundy_num += 1

        # print(num, ":", grundy_num, "!!")

        memo[num] = grundy_num

        return grundy_num, nim_s_0_lis


g_num, nim_s_0_lis = get_grundy_num(n)
if len(nim_s_0_lis) > 0:
    print(nim_s_0_lis[0])
else:
    print(-1)