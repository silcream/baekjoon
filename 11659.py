import sys

n1, n2 = map(int, sys.stdin.readline().split())


k = list(map(int, sys.stdin.readline().split()))
k2 = 0
num = [0]
for j in k:
    k2 += j
    num.append(k2)

for i in range(n2):
    a1, a2 = map(int, sys.stdin.readline().split())
    print(num[a2]-num[a1-1])