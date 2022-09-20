import sys

n, k = list(map(int, sys.stdin.readline().split()))
x = list(map(int, sys.stdin.readline().split()))
llist = sorted(x)
print(llist[-k])