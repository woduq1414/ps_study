import sys

input = sys.stdin.readline

n = int(input())

line = list(map(int, input().split()))

for i in range(n - 1):
    new_line = list(map(int, input().split()))
    new_line[0] += min(line[1], line[2])
    new_line[1] += min(line[0], line[2])
    new_line[2] += min(line[0], line[1])

    line = new_line

print(min(line))
