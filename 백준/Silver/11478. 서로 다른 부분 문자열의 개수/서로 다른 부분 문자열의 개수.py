s = input().strip()

root = {}
count = 0

for i in range(len(s)):
    node = root
    for ch in s[i:]:
        if ch not in node:
  
            node[ch] = {}
            count += 1
            
        node = node[ch]


print(count)