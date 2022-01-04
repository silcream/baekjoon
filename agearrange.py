import sys

st = int(sys.stdin.readline())
array = []
for _ in range(st):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)

    array.append((age, name))

array.sort(key = lambda x: (x[0], x[0]))

for i, j in array:
    print(i, j)

# 제대로 된 출력이 나오지만 백준은 오류로 판단
# 아마 정수와 문자열을 구분하지 않았기 때문