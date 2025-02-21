import sys
from collections import defaultdict

input = sys.stdin.readline

n, c = map(int, input().split())
arr = map(int, input().split())

dict = defaultdict(int)

for n in arr:
    dict[n] += 1

dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)

lis = []
for k, v in dict:
    for i in range(v):
        lis.append(k)

print(" ".join(map(str, lis)))

