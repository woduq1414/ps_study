import sys
input = sys.stdin.readline

n = int(input())
lis = [int(input()) for x in range(n)]
lis.sort(reverse=True)
lis2 = [x * (i+1) for (i,x) in enumerate(lis)]
result = max(lis2)
print(result)