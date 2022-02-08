import sys

n = int(sys.stdin.readline())

def mim(a, b):
    while(a != 0 and b!= 0):
        if(a>b):
            a = a%b
        else:
            b = b%a
    return a+b

num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
    num.sort()

gcd = num[1]-num[0]
for i in range(2, n):
    gcd = mim(gcd, num[i] - num[i-1])

sol = [gcd]
for i in range(2, int(gcd**0.5)+1):
    if gcd%i == 0:
        print(i, end = ' ')
        if i!= gcd//i:
            sol.insert(0, gcd//i)
for num in sol:
    print(num, end = ' ')

