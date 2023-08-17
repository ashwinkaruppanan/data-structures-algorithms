def reverseArray(arr, n):
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]   
        left += 1
        right -= 1
    return arr

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverseArray(a, len(a)))

#built in functions

#1
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b.reverse()
print(b)

#2
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = list(reversed(c))
print(d)