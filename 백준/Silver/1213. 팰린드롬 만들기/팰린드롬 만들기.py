import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

s = input()

arr = [0] * 26
for c in s:
    arr[ord(c) - ord('A')] += 1

odd_char = ""
result = ""
for i in range(26):
    c = chr(ord('A') + i)
    if arr[i] % 2 == 0:
        result += c * (arr[i] // 2)
    else:
        result += c * (arr[i] // 2)
        if odd_char == "":
            odd_char = c
        else:
            print("I'm Sorry Hansoo")
            exit()


print(result + odd_char + result[::-1])
