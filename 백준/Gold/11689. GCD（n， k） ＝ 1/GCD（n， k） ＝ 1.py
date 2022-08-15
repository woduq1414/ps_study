import math
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
t = n
divisor_set = set()

for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        divisor_set.add(i)
        n //= i
if n > 1:
    divisor_set.add(n)

s = 0
for i in range(len(divisor_set)):
    lis = list(combinations(divisor_set, i + 1))

    if i % 2 == 0:

        for a in lis:
            s += t // math.prod(a)
    else:
        for a in lis:
            s -= t // math.prod(a)

print(t - s)
