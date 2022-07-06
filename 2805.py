# 하나씩 자르기

import sys

a, b = map(int, sys.stdin.readline().split())


tree = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(tree)

while start <= end:
    mid = (start+end)//2
    i = 0
    for j in tree:
        if j >= mid:
            i += j-mid

    if i >= b:
        start = mid+1
    else:
        end = mid-1
print(end)