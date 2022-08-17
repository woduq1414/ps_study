import sys
import math

# sys.setrecursionlimit(10 ** 8)


input = sys.stdin.readline

exp = input().strip()

stack = []
result = ""

for c in exp:

    if c in ["*", "/"]:
        while len(stack) > 0 and stack[-1] in ["*", "/"]:
            result += stack.pop()
        stack.append(c)
    elif c in ["+", "-"]:

        while len(stack) > 0 and stack[-1] in ["*", "/", "+", "-"]:
            result += stack.pop()
        stack.append(c)
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while stack[-1] != "(":
            result += stack.pop()
        stack.pop()
    else:
        result += c

while len(stack) > 0:
    result += stack.pop()

print(result)
