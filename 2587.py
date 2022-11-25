import sys

k = []
for i in range(5):
    n = int(sys.stdin.readline())
    k.append(n)
k1 = sorted(k)
print(int(sum(k)/5))
print(k1[2])