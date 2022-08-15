import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
mod_cnt = [0] * m

for i in range(n):
    s += arr[i]
    mod = s % m
    mod_cnt[mod] += 1

print(int(mod_cnt[0] + sum([ x * (x-1) / 2 for x in mod_cnt ])))

