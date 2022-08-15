import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n - 1)]

t = [[] for i in range(n + 1)]
for edge in arr:
    t[edge[0]].append(edge[1])
    t[edge[1]].append(edge[0])

root = 1

parent_arr = [0] * (n + 1)


def func(root):
    for node in t[root]:
        if parent_arr[node] == 0:
            parent_arr[node] = root
            func(node)


func(1)
print(*parent_arr[2:], sep="\n")
