import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lis = list(map(int, input().split()))

lis.sort()

print(sum([
    x * (n - i) for i, x in enumerate(lis)
]))

