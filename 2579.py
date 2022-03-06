import sys

n = int(sys.stdin.readline())
k = [0 for i in range(301)]
total = [0 for i in range(301)]
for i in range(n):
    k[i] = (int(sys.stdin.readline()))

total[0] = k[0]
total[1] = k[0]+k[1]
total[2] = max(k[0]+k[2], k[1]+k[2])

for i in range(3, n):
    total[i] = max(total[i - 3] + k[i - 1] + k[i], total[i - 2] + k[i])
print(total[n-1])