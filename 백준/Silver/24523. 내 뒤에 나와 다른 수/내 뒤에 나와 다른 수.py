import sys

input = sys.stdin.readline

n = int(input())
lis = list(map(int, input().split()))

output = []

prev_num = lis[0]
c = 0

for i, num in enumerate(lis):
    if num == prev_num:
        c += 1
    else:
        output.extend([i + 1] * c)
        c = 1
        prev_num = num


output.extend([-1] * c)

print(" ".join(map(str, output)))



