import sys

n = sys.stdin.readline().split('-')
k = sum(list(map(int, n[0].split('+'))))

for i in range(1, len(n)):
    k -= sum(list(map(int, n[i].split('+'))))
print(k)