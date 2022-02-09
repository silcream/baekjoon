import sys

def binary_search(alist, blist):
    start = 0
    end = len(alist)-1

    while start<=end:
        mid = (start + end) //2
        if blist == alist[mid]:
            return 1
        elif blist > alist[mid]:
            start = mid +1
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
alist.sort()

M = int(sys.stdin.readline())
blist = list(map(int, sys.stdin.readline().split()))

for k in range(M):
    print(binary_search(alist, blist[k]))