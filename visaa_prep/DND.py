n, m = map(int,input().split())
arr = list(map(int,input().split()))
num1 = 0
num2 = 0
for x in arr:
    if (x% m == 0):
        num1 += x
    else:
        num2 += x
print(num1- num2)
