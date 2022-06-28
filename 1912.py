import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

sum = [k[0]]
for i in range(n-1):
    sum.append(max(sum[i] + k[i+1], k[i+1]))
print(max(sum))
