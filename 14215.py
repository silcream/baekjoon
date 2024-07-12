k = list(map(int, input().split()))

if max(k) >= (sum(k) - max(k)):
    k.sort()
    k[2] = k[1] + k[0] -1
    print(sum(k))
else:
    print(sum(k))