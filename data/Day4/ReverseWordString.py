# user="Hello my name is Zoya"
# splitting=user.split()
# rev=splitting[::-1]
# print(" ".join(rev))

user="Hello My Name is Zoya"
splitting=user.split()
rev=[]
for word in splitting[::-1]:
    rev.append(word[::-1])
    
print(" ".join(rev))