ma,tr,br = map(int,input().split())
max = (br-tr)//ma
if(max<0):
    print(0)
else:
    print(max)
