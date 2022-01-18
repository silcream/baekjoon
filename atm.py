import sys

N = int(sys.stdin.readline())

seq = []
seq = list(map(int, sys.stdin.readline().split()))
c = 0
seq.sort()

for i in range(N):
    for j in range(i+1):
        c += seq[j]

print(c)