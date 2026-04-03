import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

lis = list(map(int, input().split()))
arr = [0] * 2000001

x = int(input())
xdiv2 = x / 2 
for item in lis:

    if item < xdiv2:
        arr[item] = 1


print(sum([
arr[x - lis[i]] for i in range(n)
]))

