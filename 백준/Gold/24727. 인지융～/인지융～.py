import sys

input = sys.stdin.readline

n = int(input())
c, e = map(int, input().split())

fill = 1

if e < c:
    c ,e  = e, c
    fill = 2


tmp_fill = fill
other_fill = 3 - fill



arr = [ [0 for i in range(n)] for j in range(n)]


blank = 2
fill_cnt = 0


for i in range(1, 2 * n + 1):
    ii = max(i - n, 0)
    iii = -(abs(i - n) - n)
    for j in range(ii, ii + iii):

        arr[j][i - j - 1] = fill
        fill_cnt += 1
        if fill_cnt >= c:
            break
    if fill_cnt >= c:
        break
    blank += 1
blank = min(blank, n)


if n * n - c - blank - e < 0:
    print(-1)
    exit()

fill_cnt = 0
for i in range(1, 2 * n + 1):
    ii = max(i - n, 0)
    iii = -(abs(i - n) - n)
    for j in range(ii, ii + iii):

        arr[(n - 1) - j][(n - 1) - (i - j - 1)] = other_fill
        fill_cnt += 1
        if fill_cnt >= e:
            break
    if fill_cnt >= e:
        break

print(1)

for i in range(n):
    print(*arr[i], sep="")