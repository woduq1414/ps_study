import sys

input = sys.stdin.readline
a,b,c = map(int, input().split())

bin_b = str(bin(b)[2:])
bin_b = bin_b[::-1]

p = a

result = 1

for i in range(len(bin_b)):
    if bin_b[i] == '1':
        result = result * p % c

    p = p * p % c

print(result)