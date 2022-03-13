import sys
n = int(sys.stdin.readline())

k = [0] * 1000001 #공간배정  / 앞으로의 알고리즘 문제에 있어서 중요할 듯
k[1], k[2] = 1, 2

for i in range(3, n+1):
    k[i] = (k[i-2]+k[i-1])%15746
print(k[n])