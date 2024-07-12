import sys
from sys import stdin

def input():
    return stdin.readline().rstrip()

n, m = map(int, input().split())
arr_id = {}
arr_name = {}
for i in range(1, n+1):
    poket = input()
    arr_id[i] = poket
    arr_name[poket] = i

for i in range(m):
    qes = input()
    # print(type(qes))
    if qes[0].isdigit():
        print(arr_id[int(qes)])
    else:
        print(arr_name[qes])