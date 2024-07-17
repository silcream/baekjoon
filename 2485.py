import math
n = int(input())
k = []
k2 = []
for i in range(n):
    k.append(int(input()))

for i in range(1, len(k)):
    k2.append(k[i] - k[i-1])

g = k2[0]
for j in range(1, len(k2)):
    g = math.gcd(g, k2[j])

result = 0
for i in k2:
    result += i//g-1
print(result)