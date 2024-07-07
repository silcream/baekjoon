n = int(input())
for i in range(n):
    s = input()
    slen = len(s)
    if slen == 0:
        slen = 1
    print(s[0]+s[slen-1])