import sys

a = int(sys.stdin.readline())
n = set(map(int, sys.stdin.readline().split()))

b = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

for i in range(b):
    if m[i] in n:
        print(1, end=' ')
    else:
        print(0, end=' ')