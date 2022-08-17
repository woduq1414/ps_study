import math
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())



def mul(a, b):
    mul_result = [ [0] * 2 for i in range(2) ]
    mul_result[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    mul_result[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    mul_result[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    mul_result[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007
    return mul_result

result = [[1, 0], [0,1]]
t = [[1,1], [1, 0]]

n -= 1

while n > 0:
    if n % 2 == 1:
        result = mul(result, t)
    t = mul(t, t)
    n //= 2

print(result[0][0] % 1000000007)

