n = int(input())
arr = list(map(int,input().split()))
def single_num(arr):
    res = 0
    for num in arr:
        res ^= num
    return res
print(single_num(arr))
