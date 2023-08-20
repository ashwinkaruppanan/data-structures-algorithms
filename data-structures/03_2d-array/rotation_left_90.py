def rotate(mat,size):
    matOut = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        k = size-1
        for j in range(size):
            matOut[k][i] = mat[i][j]
            k -= 1

    for i in range(size):
        print(matOut[i])

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
size = 5
rotate(mat,size)