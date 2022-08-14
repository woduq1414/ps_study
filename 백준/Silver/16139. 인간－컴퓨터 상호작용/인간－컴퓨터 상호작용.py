import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 8)

st = input()
n = int(input())

arr = [[0] * 26 for i in range(len(st) + 1)]

for i, c in enumerate(st[:-1]):
    char_code = ord(c) - 97
    for j in range(26):
        arr[i + 1][j] = arr[i][j]
    
    arr[i + 1][char_code] += 1

for i in range(n):
    t = input().split()
    c, left, right = t[0], int(t[1]), int(t[2])
    char_code = ord(c) - 97

    print(arr[right + 1][char_code] - arr[left][char_code])
