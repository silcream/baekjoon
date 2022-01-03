import sys

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x, y])
# 입력받는것까지 구현
# 정렬하기

num.sort(key = lambda x: (x[0], x[1]))
# for i in range(N):
#     for j in range(N):
#         if num[i][j] > num[i+1][j]:
#             print

for i, j in num:
    print(i, j)