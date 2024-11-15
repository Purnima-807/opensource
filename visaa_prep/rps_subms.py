v,c = input().split()
chances = {'R':'P', 'P':'S', 'S':'R'}
if(v == c):
    print("NULL")
elif(chances[v] == c):
    print("Charan")
else:
    print("Vignesh")
