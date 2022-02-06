import sys

n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))

def mim(a, b):
    while(a != 0 and b!= 0):
        if(a>b):
            a = a%b
        else:
            b = b%a
    return a+b

for i in range(n-1):
    # if k[n-1] == k[i]:
    #     if k[0] == k[n-1]:
    #         print('1/1')
    #     else:
    #         break
    # else:
        print(int(k[0]/(mim(k[0], k[i+1]))), '/', int(k[i+1]/(mim(k[0], k[i+1]))), sep = '')


