n = int(input())
sticks = sorted(map(int,input().split()),reverse = True)
def largest_perimeter(sticks):
    for i in range(n-2):
        if(sticks[i] < sticks[i+1] +sticks[i+2]):
            return sticks[i] + sticks[i+1] + sticks[i+2]
    return -1
print(largest_perimeter(sticks))
    
