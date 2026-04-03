import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

lis = list(map(int,input().split()))

budget = int(input())

max_price = max(lis)

low = 0
high = max_price + 1


def get_sum(limit):
    return sum([
        min(x, limit) for x in lis
    ])


while low < high:
    mid = (low + high) // 2
    budget_sum = get_sum(mid)

    if budget_sum <= budget:
        low = mid + 1
    else:
        high = mid

print(low - 1)
