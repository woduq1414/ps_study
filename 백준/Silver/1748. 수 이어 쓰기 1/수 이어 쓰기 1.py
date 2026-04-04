import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
b = 1
result = 0
while b <= n:
    result += n - b + 1
    b *= 10
print(result)
