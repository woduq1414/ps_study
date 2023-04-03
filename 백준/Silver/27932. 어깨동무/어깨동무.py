import sys

input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr_s = [ abs(arr[i+1] - arr[i]) for i in range(n-1) ]

def func(h):
    s = 0
    p_f = False
    for i in range(n-1):
        if arr_s[i] > h:

            if p_f:
                s += 1
            else:
                s += 2
            p_f = True
        else:
            p_f = False

    return s


l = 0
r = 10 ** 9

while l < r:
    mid = (l + r) // 2

    if func(mid) <= k:
        r = mid
    else:
        l = mid + 1

print(l)