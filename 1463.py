import sys
n = int(sys.stdin.readline())
k = [0, 0, 1, 1]

for i in range(4, n+1):
    k.append(k[i-1] + 1)

    if i % 2 == 0:
        k[i] = min(k[i], k[i//2] + 1)

    if i % 3 == 0:
        k[i] = min(k[i], k[i//3] + 1)

print(k[n])

# 배열 쓰기
# min 쓰기

#다이나믹 프로그래밍

