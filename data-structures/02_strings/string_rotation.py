#left rotation
def rotateString(str,rotation,length):
    return str[rotation:] + str[:rotation]

str = "abcde"
rotation = 2
print(rotateString(str,rotation, len(str)))

