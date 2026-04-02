import sys

input = lambda: sys.stdin.readline().rstrip()

line = input()

splitted = line.split("-")
# print(splitted)

result = 0
for i, part in enumerate(splitted):
    part_splitted = list(map(int,part.split("+")))
    if i == 0:
        result += sum(part_splitted)
    else:
        result -= sum(part_splitted)

print(result)