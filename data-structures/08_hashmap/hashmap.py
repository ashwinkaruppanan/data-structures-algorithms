names = ["Alice", "Bob", "Charlie", "David", "Eve", "Alice", "Frank", "Grace", "Helen"]

namesMap = {}
for i in names:
    if i in namesMap:
        namesMap[i] += 1
    else:
        namesMap[i] = 1
    
print(namesMap)