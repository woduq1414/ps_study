import sys
input = sys.stdin.readline

n, m = map(int, input().split())


lis = [[0] * m for i in range(n)]
for i in range(2):
    for j in range(n):
        line = list(map(int, input().split()))

        for k in range(m):
            lis[j][k] += line[k]


for i in range(n):
    print(" ".join([str(x) for x in lis[i]]))