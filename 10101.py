a = []
for i in range(3):
    k = int(input())
    a.append(k)

if a.count(60) == 3:
    print('Equilateral')
elif sum(a) == 180 and len(set(a)) == 2:
    print('Isosceles')
elif sum(a) == 180 and len(set(a)) == 3:
    print('Scalene')
#set으로 바꾸고 len해서 길이가 2면 중복하나 있어서 고유한 수는 2개 있다는 거임 3이면 각각 다른 수라는뜻
else:
    print('Error')

