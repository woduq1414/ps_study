import sys
from bisect import bisect_right

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = list(map(int, input().split()))
budget = int(input())

max_price = max(lis)

def get_sum(limit):
    return sum(min(x, limit) for x in lis)

answer = bisect_right(range(max_price + 1), budget, key=get_sum) - 1
print(answer)