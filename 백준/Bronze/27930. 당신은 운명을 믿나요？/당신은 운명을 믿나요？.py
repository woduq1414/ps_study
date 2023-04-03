import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

s = input()

cnt1 = 0
cnt2 = 0

s1 = "YONSEI"
s2 = "KOREA"


for c in s:
    if c == s1[cnt1]:
        cnt1 += 1
    if c == s2[cnt2]:
        cnt2 += 1

    if cnt1 == 6:
        print("YONSEI")
        exit()
    if cnt2 == 5:
        print("KOREA")
        exit()