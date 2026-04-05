import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

queue = deque()

for i in range(n):
    queue.append(i + 1)

last_popped = None
while True:
    last_popped = queue.popleft()

    if queue:
        queue.append(queue.popleft())
    else:
        break

print(last_popped)

