import sys

N, K = map(int, sys.stdin.readline().split())

def c(N):
    if N<=1:
        return 1
    return N * c(N-1)
    

print(c(N) // (c(K) * c(N-K)))
