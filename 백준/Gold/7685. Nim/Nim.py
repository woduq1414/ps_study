import sys

input = sys.stdin.readline

while True:

    n = int(input())

    if n == 0:
        break

    arr = list(map(int, input().split()))

    c = 0
    nim_s = 0
    for i in range(n - 1):
        nim_s ^= arr[i]

    if nim_s < arr[n - 1]:
        c += 1

    for i in range(n - 2, -1, -1):
        nim_s = nim_s ^ arr[i] ^ arr[i + 1]
        if nim_s < arr[i]:
            c += 1
    print(c)