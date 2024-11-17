n = int(input())
arr = list(map(int,input().split()))
k = int(input())
def rotate_arr(arr,k):
    k = k%n
    return arr[-k:] + arr[:-k]
print(*rotate_arr(arr,k))
