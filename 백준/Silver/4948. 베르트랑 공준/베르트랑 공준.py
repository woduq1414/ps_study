import sys

input = sys.stdin.readline



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


lis = is_prime_num(123456 * 2)
lis2 = []
c = 0

for b in lis:
    if b is True:
        c += 1
    lis2.append(c)




while True:
    n = int(input())

    if n == 0:
        break
    else:
        print(lis2[2 * n] - lis2[n])
