import sys
#리스트 안에서의 크기 순서
N = int(sys.stdin.readline())
cnt = 0
coor = list(map(int, sys.stdin.readline().split()))
count_list = []

#생각해보니까 입력해서 확인할 필요 없는것 같음
#문제 해석 - 같이 입력된 숫자들 중에서 자기보다 작은 숫자 개수 프린트함 순서대로 -> 배열이 중요

count_list = sorted(list(set(coor))) #집합자료형의 특징 : 중복허용x , 순서가 없음 -> 리스트화 -> 정렬
dic = {count_list[i] : i for i in range(len(count_list))} #딕셔너리로 개수배열을 만듦


for i in coor:
    print(dic[i], end = ' ')

