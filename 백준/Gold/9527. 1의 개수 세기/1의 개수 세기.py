import sys
import math
from decimal import *


input = sys.stdin.readline

a, b = map(int, input().split())

dp = [1]

for i in range(1, 100):

    c = Decimal(2 ** i)
    d = Decimal(i)


    dp.append(Decimal(c * d / 2 + 1))

# print(dp)

def func(n):
    if n == 0:
        return 0

    l2 = n.bit_length() - 1
    # print(l2)
    s = Decimal(0)

    # arr = []
    #
    # while n >= 1:
    #     if n % 2 == 1:
    #         arr.append(1)
    #     else:
    #         arr.append(0)
    #     n //= 2
    arr = str(bin(n))[2:]

    # print(arr)

    c = 0

    for i in range(l2 + 1):

        if arr[i] == '1':
            s += Decimal(dp[l2 - i])
            for _ in range(c):

                x = Decimal(2)
                y = Decimal(l2 - i)

                s += Decimal(x ** y)
            # print(dp[l2 - i] + c * (2 ** (l2 - i)))
            c += 1
    return s


print(func(b) - func(a - 1))

# for i in range(1, 100):
#     c , d = func(2 ** i), func(2 ** i - 1)
#     print(i,2 **i,  c,d, c - d)


# for i in range(40, 60):
#     p = 1
#     for j in range(i):
#         p *= 2
#     q = pow(2, i)
#     print(i, p, q, p - q)
#





# c = 0
# for i in range(1, 10000):
#
#     c += str(bin(i))[2:].count('1')
#
#     print(i, func(i), c)
#
#     if func(i) != c:
#         print("!!!!!!!!!!!!")
#         exit()
