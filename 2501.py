n, m = map(int,input().split())
k = []
for i in range(1, n+1):
    if (n%i == 0):
        k.append(i)
# if k[m-1] != None:
#     print(k[m-1])
# else:
#     print(0)
# print(len(k)<m)
if len(k)<m:
    print(0)
else:
    print(k[m - 1])