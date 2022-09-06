import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))



def even_get_grundy_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 1 - n % 2



def odd_get_grundy_num(n):
    if n == 3:
        return 1

    if n % 2 == 1:
        return 0

    c = 0
    while n % 2 == 0:

        n //= 2
        c += 1

    if n == 3:
        return 1 + c % 2

    return 2 - c % 2



nim_s = 0
for num in arr:
    if k % 2 == 0:
        nim_s ^= even_get_grundy_num(num)
    else:
        nim_s ^= odd_get_grundy_num(num)
if nim_s == 0:
    print("Nicky")
else:
    print("Kevin")