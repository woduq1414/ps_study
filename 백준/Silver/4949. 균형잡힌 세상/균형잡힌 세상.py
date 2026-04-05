import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

while True:
    line = input()

    if line == ".":
        break
    
    stack = []
    for c in line:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
    
    print("no" if stack else "yes")