import sys


input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0

current = 0

result = []

while start != n:

    if start == end:

        end += 1
        current += arr[end - 1]
    else:
        if current >= s:
            result.append(end - start)

            start += 1
            current -= arr[start - 1]
        elif end == n:
            start += 1
            current -= arr[start - 1]
        else:
            end += 1
            current += arr[end - 1]

if result:
    print(min(result))
else:
    print(0)
