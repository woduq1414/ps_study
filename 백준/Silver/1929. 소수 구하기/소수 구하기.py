import sys

input = sys.stdin.readline

a, b = map(int, input().split())


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


lis = is_prime_num(b) 
for i in range(a, b + 1):
    if lis[i] is True:
        print(i)
