def search(mat,size, target):
    for i in range(size):
        for j in range(size):
            if mat[i][j] == target:
                print(f"Target value in row:{i+1} column:{j+1}")
                return
mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
size = 5
target = 22
search(mat,size, target)