import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
k = a + (m // 60)
l = b+(m%60)

if b+m<60:
    print(k, l)
else:
    if l > 59:
        l = l - 60
        k = k+1
    if k > 23:
        print(k-24, l)
    else:
        print(k, l)