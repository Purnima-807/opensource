n = int(input())
arr = list(map(int,input().split()))
balance_arr = []
for i in range(n):
    right_wg = sum(arr[i+1:])
    left_wg = sum(arr[:i])
    bal = abs(left_wg - right_wg)
    balance_arr.append(bal)
print(*balance_arr)
