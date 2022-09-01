import sys

input = sys.stdin.readline


T = int(input())
arr = [ int(input()) for _ in range(T)]

g_arr = [0,0,1,1]


for i in range(4, max(arr) + 1, 1):

    group = [0] * 5001
    for j in range(i - 2):
        group[g_arr[j] ^ g_arr[i - 2 - j]]= 1
    g_num = 0
    while group[g_num]== 1:
        g_num += 1

    g_arr.append(g_num)

for i in range(T):
    print(["First","Second"][g_arr[arr[i]]== 0])