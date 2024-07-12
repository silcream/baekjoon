import sys
from sys import stdin
from collections import Counter

def input():
    return stdin.readline().rstrip()

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

count = Counter(arr1)
for i in range(m):
    if arr2[i] in count:
        print(count[arr2[i]], end = ' ')
    else:
        print(0, end = ' ')

