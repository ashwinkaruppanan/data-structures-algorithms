def transpose(mat, size):
    for i in range(size):
        for j in range(i,size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    for i in range(size):
        print(mat[i])

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
size = 5
transpose(mat, size)



