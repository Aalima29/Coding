user=input("Enter Any Sentence: ")
splitting=user.split()

for i in range(len(splitting)):
    splitting[i]=splitting[i].lower()
splitting.sort()
print(splitting)