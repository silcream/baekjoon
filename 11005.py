n, m = map(int,input().split())

s = ''
ss = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while n>0:
    s += str(ss[n%m])
    n //=m

print(s[::-1])