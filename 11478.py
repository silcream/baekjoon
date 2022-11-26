import sys

s = input()
kk = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        kk.add(s[i:j+1])

print(len(kk))