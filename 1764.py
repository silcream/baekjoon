n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    k = input()
    a.add(k)
for j in range(m):
    k = input()
    b.add(k)
c = sorted(list(a & b))
print(len(c))

for i in c:
    print(i)