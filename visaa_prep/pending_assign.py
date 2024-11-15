X,Y,Z = map(int,input().split())
time = (Z*24*60)
if (X*Y <= time):
    print("YES")
else:
    print("NO")
