import math
m = int(input())


def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
# 소수인지 확인

for i in range(m):
    a = int(input())
    while True:
        if prime(a):
            print(a)
            break
        else:
            a+=1
# 소수가 아니면 +1 해서 다음 숫자가 소수인지 확인