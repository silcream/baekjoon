import sys
from collections import Counter

N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())
    c = []
    for j in range(n):
        a, b = sys.stdin.readline().split()
        c.append(b)

    wearcount = Counter(c)
    cnt = 1

    for l in wearcount:
        cnt *= wearcount[l] +1

    print(cnt-1)
