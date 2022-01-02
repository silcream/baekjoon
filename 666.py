'''
N = map(int,input().split())

sequence = []
sixseq = []

for i in range(10000):
    sequence.append(i)
    for j in range(3):
        if ((sequence[j] == sequence[j+1])and(sequence [j+1] == sequence [j+2])and(sequence [j+2] == 6)):
            sixseq.append[j]
        else:
            sequence = []


print(sixseq[N]) '''

# 실행되지 않는 코드이다 나는 배열에 넣어서 풀려고 했는데 너무 어렵게 접근하고 있다는 걸 알았다

N = int(input())
num = 666
cnt = 0

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
