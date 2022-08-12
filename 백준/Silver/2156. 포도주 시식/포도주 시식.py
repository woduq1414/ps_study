import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


n = int(input())

memo = {}

arr = [int(input()) for i in range(n)]

def func(idx):

    if idx in memo:
        return memo[idx]
    else:

        if idx >= n - 3:
            result = arr[idx]
        else:
            result = arr[idx] + min(func(idx + 1), func(idx + 2),func(idx + 3))
        memo[idx] = result



        return result

if len(arr) <= 2:
    print(sum(arr))
else:
    print(sum(arr) - min(func(0), func(1), func(2)))



