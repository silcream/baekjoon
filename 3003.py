import sys

n = list(map(int, sys.stdin.readline().split()))
k = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(k[i]-n[i], end = ' ')
