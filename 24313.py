f, g = map(int,input().split())
c = int(input())
n0 = int(input())


if f*n0+g <= c*n0 and f <= c:
    print(1)
else:
    print(0)