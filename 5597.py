import sys

k = []
for i in range(28):
    k.append(int(sys.stdin.readline()))


for i in range(1, 31):
    if i not in k:
        print(i)
