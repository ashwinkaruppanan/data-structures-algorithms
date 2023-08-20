def reverseString(str,length):
    rev = ""
    for i in range(length-1,-1,-1):
        rev += str[i]
    return rev

def isPalindrome(str1,str2):
    if str1 == str2:
        return "Given string is palindrome"
    return "Given string is not a palindrome"

str = "python"
print(reverseString(str, len(str)))

#slicing - efficient way
print(str[::-1])

#check palindrome
print(isPalindrome(str,str[::-1]))