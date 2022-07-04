import sys

input = sys.stdin.readline

h, m, s = map(int, input().split())

d = int(input())

delta_s = d % 60
delta_m = d % 3600 // 60
delta_h = d // 3600

h, m, s = h + delta_h, m + delta_m, s + delta_s

m, s = m + s // 60, s % 60
h, m = h + m // 60, m % 60
h = h % 24

print(f"{h} {m} {s}")
