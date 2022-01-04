import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x, y])

num.sort(key = lambda x: (x[1], x[0])) # y좌표 기준으로 정렬

for i, j in num:
    print(i, j)