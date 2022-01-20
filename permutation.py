
import sys

N = int(sys.stdin.readline())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    print(factorial(m)//(factorial(n) * factorial(m - n)))
