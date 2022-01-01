N, M = map(int,input().split())

chess = []
count = []

for _ in range(N):
    chess.append(input())

for a in range(N-7):
    for b in range(M-7):
        case1 = 0
        case2 = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if ((i+j)%2 == 0):
                    if chess[i][j] != 'W':
                        case1 += 1
                    if chess[i][j] != 'B':
                        case2 += 1
                else:
                    if chess[i][j] != 'B':
                        case1 += 1
                    if chess[i][j] != 'W':
                        case2 += 1

        count.append(min(case1, case2))

print(min(count))

