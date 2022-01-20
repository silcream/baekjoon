import sys

N = int(sys.stdin.readline())
seq = []
seq = list(map(int, sys.stdin.readline().split()))
seq.sort()
if N == 1:
    print(seq[0]*seq[0])
else:
    print(seq[0]*seq[N-1])