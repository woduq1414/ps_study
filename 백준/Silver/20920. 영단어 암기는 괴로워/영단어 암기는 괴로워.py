from collections import defaultdict 

n, m = map(int, input().split())
lis = []

counter = defaultdict(int)

for i in range(n):
    word = input().strip()
    if len(word) >= m:
        lis.append(m)
        counter[word] += 1


sorted_list = sorted(counter.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

print("\n".join([x[0] for x in sorted_list]))