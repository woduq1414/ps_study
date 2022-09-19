import sys

input = sys.stdin.readline

n = int(input())
arr_i = map(int, input().split())


def is_prime_num(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i * j] = False
                j += 1

    return arr


lis = is_prime_num(1000)
c = 0
for n in arr_i:
    if lis[n] is True:
        c += 1
print(c)
