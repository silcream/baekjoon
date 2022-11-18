import sys
A = []

for row in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)
maxthing = 0
for i in range(9):
    for j in range(9):
        if A[i][j] > maxthing:
            maxthing = A[i][j]
print(maxthing)
for i in range(9):
    for j in range(9):
        if maxthing == A[i][j]:
            print(i+1, j+1)
            break
