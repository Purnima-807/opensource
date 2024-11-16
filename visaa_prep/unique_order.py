from collections import OrderedDict
n = int(input())
arr = list(map(int,input().split()))
unique_arr = list(OrderedDict.fromkeys(arr))
print(*unique_arr)
