n, m = map(int,input().split())
t = []
for i in range(n):
    t.append(i+1)

for i in range(m):
    c = 0
    a, b = map(int, input().split())
    c = t[a-1:b]
    c.reverse()
    t[a-1:b] = c

for i in range(n):
    print(t[i], end = ' ')