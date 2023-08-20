def search(arr, value,n):
    for i in range(n):
        if arr[i] == value:
            return f"Item found in postion: {i}"
    return "Item not found"

def insertEnd(arr,value,n):
    arr.append(value)

def removeEnd(arr,n):
    if n > 0:
        arr[n-1] = 0
    

def insertMiddle(arr, position, value,n):
    for i in range(n-1,position-1,-1):
        arr[i + 1] = arr[i]
    arr[position] = value

def reomveMiddle(arr,position,n):
    for i in range(position,n):
        arr[i - 1] = arr[i]

arr = [12, 34, 10, 6, 3,40,0]
n = len(arr)

# #search in array
# search(arr,3,n)

# #insert value at end
# n = len(arr)
# insertEnd(arr,99,n)

# #remove value at end 
# removeEnd(arr,n)

#insert value at middle 
# insertMiddle(arr,3,20,n-1)

#remove value at middle
reomveMiddle(arr,2,n)
