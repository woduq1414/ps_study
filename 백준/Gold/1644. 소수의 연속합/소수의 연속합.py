import sys


input = sys.stdin.readline

n = int(input())

def is_prime_num(n):
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr

arr = [ i for i ,x in enumerate(is_prime_num(n)) if x is True ]

start = 0
end = 0

current = 0

result = 0

while start != len(arr):

    if start == end:

        end += 1
        current += arr[end - 1]
    else:
        if current >= n:
            if current == n:
                result += 1



            start += 1
            current -= arr[start - 1]
        elif end == len(arr):
            start += 1
            current -= arr[start - 1]
        else:
            end += 1
            current += arr[end - 1]

print(result)
