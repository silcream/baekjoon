def recursion(s, l, r):
    global cnt
    cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


import sys


n = int(sys.stdin.readline())
for i in range(n):
    k = sys.stdin.readline().rstrip()
    cnt = 0
    print(isPalindrome(k), cnt)