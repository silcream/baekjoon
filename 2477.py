import sys

k = int(sys.stdin.readline())
height = []
width = []

total = []

for i in range(6):
    dir, length = map(int, sys.stdin.readline().split())
    if dir == 1 or dir == 2:
        height.append(length)
        total.append(length)
    else:
        width.append(length)
        total.append(length)

big = max(height) * max(width)

maxhei = total.index(max(height))
maxwid = total.index(max(width))
small1 = abs(total[maxhei-1]) - total[(maxhei-5 if maxhei == 5 else maxhei+1)]
small2 = abs(total[maxwid-1]) - total[(maxwid-5 if maxwid == 5 else maxwid+1)]
small = abs(small1 * small2)

area = big - small

print(area*k)