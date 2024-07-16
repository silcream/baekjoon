import sys
from sys import stdin

def input():
    return stdin.readline().rstrip()
#
# c = int(input())
# count = 0
# for i in range(c):
#     for j in range(int(c/2)):
#         if i == j**2:
#             count += 1
# print(count-1)

print(int(int(input())**0.5))