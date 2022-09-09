import sys


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    data = list(map(int, input().split()))
    n, arr = data[0], data[1:]

    if len(arr) <= 4:
        print("YES")
    else:
        x, y, z, w = arr[0:4]

        a = (w - x + 3 * y - 3 * z) / 6
        b = (-2 * w + 3 * x - 8 * y + 7 * z) / 2
        c = (11 * w - 26 * x + 57 * y - 42 * z) / 6
        d = -w + 4 * x - 6 * y + 4 * z

        f = True
        for i in range(4, len(arr)):
            j = i + 1
            answer = a * (j ** 3) + b * (j ** 2) + c * j + d
            if abs(arr[i] - answer) >= 0.00001:
                f = False

        if f is False:
            print("NO")
        else:
            print("YES")
