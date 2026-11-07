import keyword
word=["break","John","continue","try","leo","else","while","if","xo"]
for i in range(len(word)):
    if keyword.iskeyword(word[i]):
        print(word[i],"Is a keyword in python")
    else:
        print("Not a keyword")