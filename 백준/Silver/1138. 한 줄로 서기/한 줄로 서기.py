import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

lis = list(map(int,input().split()))
arr = [-1] * n
for i in range(n):
    
    cnt = 0
    j = 0
    while cnt <= lis[i]:
        if arr[j] == -1:
            cnt += 1
        j += 1
    
    arr[j- 1] = i + 1


print(*arr, sep=" ")