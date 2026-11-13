user=input("Enter a String")
freq={}
splitting=user.split()

for word in splitting:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("Freq of words are ",freq)