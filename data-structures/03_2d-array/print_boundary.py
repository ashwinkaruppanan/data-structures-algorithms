def boundary(mat,size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size -1 or j == 0 or j == size - 1:
                print(mat[i][j],end=" ")
            else:
                print(" ",end=" ")
        print()

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
size = 5
boundary(mat,size)