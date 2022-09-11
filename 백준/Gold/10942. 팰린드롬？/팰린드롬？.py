import sys


input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())


dp = [ [] for i in range(n + 1) ]
dp[1] = [ x for x in range(n)]

if n >= 2:

    dp[2] = [ x for x in range(n - 1) if arr[x] == arr[x + 1]]

    for i in range(3, n + 1, 1):
        for s in dp[i - 2]:
            a, b = s, s + i - 3
            if a == 0 or b == n - 1:
                continue
            else:
                if arr[a - 1] == arr[b + 1]:
                    dp[i].append(a - 1)


for i in range(m):
    s, e = map(int,input().split())
    l = e - s + 1
    if s - 1 in dp[l]:
        print(1)
    else:
        print(0)