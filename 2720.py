n = int(input())
for i in range(n):
    c = int(input())
    print(int(c/25), int(c%25/10), int(c%25%10/5),int(c%10%5))