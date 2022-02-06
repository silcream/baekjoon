# import sys
# import math
#
# n, m = map(int, sys.stdin.readline().split())
# num = math.comb(n, m)
# k = []
# cnt = 0
# for i in str(num):
#     k.append(i)
# for j in range(len(k)):
#     if k[len(k)-j-1] == '0' :
#         cnt += 1
#     else:
#         break
#
# print(cnt)
#

#위의 코드는 되는 코드인데 시간초과가 뜬다
# 문제가 원하는 것 은 2의 배수와 5의 배수의 조합이다
import sys


def five(n):
    a = 0
    while n != 0:
        n = n//5
        a += n
    return a

def two(n):
    a = 0
    while n != 0:
        n = n//2
        a += n
    return a

n, m = map(int, sys.stdin.readline().split())

if m == 0:
    print(0)
else:
    print(min(two(n) -two(m)-two(n-m), five(n)-five(m)-five(n-m)))