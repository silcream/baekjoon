import sys

a, b = map(int, sys.stdin.readline().split())

aset = set(map(int, sys.stdin.readline().split()))
bset = set(map(int, sys.stdin.readline().split()))

print(len(aset-bset) + len(bset-aset))