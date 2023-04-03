import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()
# subsum = [0]
subs = [0]
for i in range(1, n):
    subs.append(li[i]-li[i-1])
    # subsum.append(subs[i-1]+li[i]-li[i-1])

def getsubs(a, b):
    return subsum[b]-subsum[a]

even_min = float('inf')
odd_min = float('inf')

for i in subs[1:]:
    if i % 2 == 0 and even_min > i:
        even_min = i
    if i % 2 != 0 and odd_min > i:
        odd_min = i

if even_min == float('inf'):
    for i in range(1, n-1):
        even_min = min(even_min, subs[i]+subs[i+1])


print(even_min if even_min != float('inf') else -1, odd_min if odd_min != float('inf') else -1)