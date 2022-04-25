import sys

n = int(sys.stdin.readline())

k = []

for i in range(n):
    a= sys.stdin.readline().split()
    if a[0] == 'push':
        k.append(a[1])
    elif a[0] == 'top':
        if len(k) == 0:
            print(-1)
        else:
            print(k[-1])
    elif a[0] == 'size':
        print(len(k))
    elif a[0] == 'empty':
        if len(k) == 0:
            print(1)
        else:
            print(0)
    elif a[0] =='pop':
        if len(k) == 0:
            print(-1)
        else:
            print(k.pop())