import sys


n = int(sys.stdin.readline())
arr = [[0]*100 for _ in range(101)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1


count = 0
for row in arr:
    count += row.count(1)
print(count)


