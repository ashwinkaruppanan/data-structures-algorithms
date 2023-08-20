#A lexicographic pattern refers to a pattern that follows the order of characters as they appear in a alphabet

def follows_lexicographic_pattern(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

string = "abcde"
if follows_lexicographic_pattern(string):
    print("The string follows a lexicographic pattern.")
else:
    print("The string does not follow a lexicographic pattern.")
