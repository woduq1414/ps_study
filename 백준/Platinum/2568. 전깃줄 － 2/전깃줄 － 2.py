import sys

import bisect

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

arr.sort(key=lambda x: x[0])
temp_arr = arr

arr = [x[1] for x in arr]

c = [10 ** 9] * (n + 1)
c[0] = -10 ** 9
c[1] = arr[0]
longest_len = 1

pos_arr = [-1] * (n + 1)
pos_arr[1] = 1

for i, num in enumerate(arr[1:]):
    # print(i, num, c, cc)

    if c[longest_len] < num:
        c[longest_len + 1] = num
        pos_arr[i + 2] = longest_len + 1

        longest_len += 1
    else:
        idx = bisect.bisect_left(c, num)
        c[idx] = num

        pos_arr[i + 2] = idx

print(n - longest_len)


lis = [-1] * longest_len

t = longest_len

for i in range(len(pos_arr) - 1, -1, -1):

    pos = pos_arr[i]
    if t == pos:
        lis[pos - 1] = arr[i - 1]
        t -= 1

result = []
for i in range(n):
    if temp_arr[i][1] not in lis:
        result.append(temp_arr[i][0])

print(*result, sep="\n")
