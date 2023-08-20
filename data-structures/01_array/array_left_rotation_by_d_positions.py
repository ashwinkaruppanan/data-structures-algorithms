def rotate(arr,n,d):
    temp = arr[:d]
    ind = 0
    valPos = d
    while(ind < n - d):
        arr[ind] = arr[valPos]
        ind += 1
        valPos += 1
    valPos = 0
    while(ind < n):
        arr[ind] = temp[valPos]
        ind += 1
        valPos += 1
    return arr 

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
print(rotate(arr,len(arr), d))


