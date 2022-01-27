import sys


n = int(sys.stdin.readline())
i = 0
j = 5

def tri(N):
    seq = [1, 1, 1, 2, 2]
    for i in range(N):
        for j in range(N):
            seq.append(seq[i-1] + seq[j])
    return seq[N-1]

for i in range(n):
    N = int(sys.stdin.readline())
    print(tri(N))
