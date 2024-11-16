n = int(input())
arr = list(map(int,input().split()))
rot_arr = arr[1:] + arr[:1]
print(*rot_arr)
