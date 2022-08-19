import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

#
# def get_triangle_area(c1, c2, c3):
#     return abs((c1[0] * c2[1] + c2[0] * c3[1] + c3[0] * c1[1]) - (
#             c1[1] * c2[0] + c2[1] * c3[0] + c3[1] * c1[0])) / 2
#

s = 0

arr.append([arr[0][0], arr[0][1]])

for i in range(0, n):
    s += arr[i][0] * arr[i + 1][1] - arr[i][1] * arr[i+1][0]

print(format(abs(s / 2), ".1f"))
