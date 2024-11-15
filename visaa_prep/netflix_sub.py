A,B,C,X = list(map(int,input().split()))
if((A+B) | (B+C) | (C+A) >= X):
    print("YES")
else:
    print("NO")
