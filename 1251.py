st = input().strip()
n = len(st)
sword  =None
for i in range(1, n-1):
    for j in range(i+1, n):
        p1 = st[:i][::-1]
        p2 = st[i:j][::-1]
        p3 = st[j:][::-1]

        word = p1+p2+p3

        if sword is None or word < sword:
            sword = word

print(sword)
