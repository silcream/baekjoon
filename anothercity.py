import sys

N = int(sys.stdin.readline())

road = []
cost = []

road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
res = 0
c = cost[0]
for i in range(N-1):
    if c>cost[i]:
        c = cost[i]
    res += c*road[i]

print(res)