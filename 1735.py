import math


a, b = map(int, input().split())
c, d = map(int, input().split())
n = math.gcd(a*d+c*b, b*d)
print((a*d+c*b)//n, (b*d)//n)