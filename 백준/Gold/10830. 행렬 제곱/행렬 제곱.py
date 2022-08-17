import math
import sys
from itertools import combinations

input = sys.stdin.readline

n, b = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]


def mul(a, b):
    mul_result = [[0] * len(b[0]) for i in range(len(a))]
    for i in range(len(mul_result)):
        for j in range(len(mul_result[i])):
            for k in range(len(a[i])):
                mul_result[i][j] += a[i][k] * b[k][j]
            mul_result[i][j] %= 1000
    return mul_result


result = [[(0 if i != j else 1) for j in range(n)] for i in range(n)]


while b > 0:
    if b % 2 == 1:
        result = mul(result, arr)
    arr = mul(arr, arr)
    b //= 2

for i in range(n):
    print(*result[i], sep=" ")
