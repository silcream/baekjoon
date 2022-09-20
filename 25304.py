import sys

total = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    total = total - (a*b)

if total == 0:
    print('Yes')
else:
    print('No')
