import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    def mim(a, b):
        while(a != 0 and b!= 0):
            if(a>b):
                a = a%b
            else:
                b = b%a
        return a+b

    print(int(a*b/(mim(a, b))))