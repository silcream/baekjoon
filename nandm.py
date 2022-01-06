import sys
import itertools
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num = []

for i in range(N):
    num.append(i+1)

K = itertools.permutations(num, M)
K = list(K)

for i in K:
    print(' '.join(map(str, i)))

#print의 과정이 어려웠던 문제다
#파이썬의 내장함수로 쉽게 구할 수 있었다

# while i < len(K):
#     print(*K[i])
#     i += 1
