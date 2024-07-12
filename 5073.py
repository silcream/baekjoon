while(1):
    k = list(map(int, input().split()))
    a = k[0]
    b = k[1]
    c = k[2]
    if a == b == c == 0:
        break
    elif max(k) >= (sum(k) - max(k)):
        print('Invalid')
    elif len(set(k)) == 1:
        print('Equilateral')
    elif len(set(k)) == 2:
        print('Isosceles')
    elif len(set(k)) == 3:
        print('Scalene')
