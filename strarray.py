import sys

st = int(sys.stdin.readline())
array = []
for _ in range(st):
    array.append(sys.stdin.readline().strip()) #strip() : 동일한 문자 제거
#set : 중복 허용하지 않음
arrayset = set(array)
array = list(arrayset)
array.sort()
array.sort(key = len)

for i in array:
    print(i)