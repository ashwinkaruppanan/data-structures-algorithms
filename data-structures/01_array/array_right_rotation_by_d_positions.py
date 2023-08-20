def rotate(arr,n,d):
    temp = arr[n-d:]
    ind = n-1
    valPos = n-d-1
    while(ind > -1):
        arr[ind] = arr[valPos]
        ind -= 1
        valPos -= 1
    ind = d-1
    valPos = len(temp) - 1
    while(ind >= 0):
        arr[ind] = temp[valPos]
        ind -= 1
        valPos -=1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
print(rotate(arr,len(arr), d))


