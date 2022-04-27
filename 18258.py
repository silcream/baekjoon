import sys

n = int(sys.stdin.readline())
k = []
cnt = 0

for i in range(n):
    a= sys.stdin.readline().split()
    if a[0] == 'push':
        k.append(a[1])
    elif a[0] == 'size':
        print(len(k)-cnt)
    elif a[0] == 'empty':
        if len(k)-cnt == 0:
            print(1)
        else:
            print(0)
    elif a[0] =='pop':
        if len(k)-cnt == 0:
            print(-1)
        else:
            print(k[cnt])
            cnt += 1
    elif a[0] =='front':
        if len(k)-cnt == 0:
            print(-1)
        else:
            print(k[cnt])
    elif a[0] =='back':
        if len(k)-cnt == 0:
            print(-1)
        else:
            print(k[-1])