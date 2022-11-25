import sys

a, b = map(int, sys.stdin.readline().split())

s = set([sys.stdin.readline() for _ in range(a)])
cnt = 0
for _ in range(b):
    t = sys.stdin.readline()
    if t in s:
        cnt += 1
print(cnt)