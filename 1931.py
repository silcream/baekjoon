import sys

n = int(sys.stdin.readline())

k = []
for i in range(n):
    k.append(list(map(int, sys.stdin.readline().split())))

k.sort(key=lambda x: (x[1], x[0]))

cnt = 0
t = 0

for i in range(n):
    if t <= k[i][0]:
        t = k[i][1]
        cnt += 1

print(cnt)
