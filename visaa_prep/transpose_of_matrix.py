n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
tr = [[row[i] for row in matrix] for i in range(n)]
for row in tr:
    print(*row)
