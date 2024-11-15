n = int(input())
mat = [input().split() for i in range(n)]
mirr_mat= [row[::-1] for row in mat]
for row in mirr_mat:
    print(' '.join(row))
