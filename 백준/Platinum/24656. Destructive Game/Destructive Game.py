import sys

input = sys.stdin.readline

n = int(input())

nim_s = 0

for _ in range(n):

    s, k = map(int, input().split())

    r = s % (k + 1)

    g_num = 0
    if r == k and k % 2 == 0:
        g_num = 2
    else:
        g_num = r % 2

    nim_s ^= g_num

if nim_s == 0:
    print("Bob")
else:
    print("Alice")