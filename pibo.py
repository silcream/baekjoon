import sys

c0 = [1, 0]
c1 = [0, 1]

n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())

    if (k == 0):
        print('1 0')
    elif (k == 1):
        print('0 1')
    else:
        for j in range(2, k+1):
            c0.append(c0[j-1] + c0[j-2])
            c1.append(c1[j-1] + c1[j-2])
        print(f'{c0.pop()} {c1.pop()}')
        c0 = [1, 0]
        c1 = [0, 1]