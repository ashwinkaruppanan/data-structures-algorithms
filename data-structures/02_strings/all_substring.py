def substring(str, length):
    for i in range(length):
        for j in range(i,length):
            print(str[i:j+1])

str = "geeks"
length = len(str)
substring(str,length)

#output

# g
# ge
# gee
# geek
# geeks
# e
# ee
# eek
# eeks
# e
# ek
# eks
# k
# ks
# s