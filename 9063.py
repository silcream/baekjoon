n = int(input())
q = []
w = []
for i in range(n):
    a, b = map(int,input().split())
    q.append(a)
    w.append(b)
print((max(q)-min(q)) *(max(w)-min(w)))