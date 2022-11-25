import sys


a, b = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    low_arr = mergesort(arr[:mid])
    high_arr = mergesort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l+= 1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return print(merged_arr)

mergesort(k)

for i in range(a):
    if k[i] > b:
        print(-1)
        
print(mergesort(k))
#
# def merge_sort(k):
#     kmid = int(len(k)/2)
#     if k[0] < k[-1]:
#         merge_sort((k, k[0]))
#         merge_sort((k, k[0]))
#         merge((k, k[0]))
#
# def merge(A, k[0], kmid, k[-1]):
#
