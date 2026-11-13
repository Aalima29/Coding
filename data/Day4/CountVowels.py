user=input("Enter a String : ")
vowels="aeiou"
dict={}.fromkeys(vowels,0)

for char in user:
    if char in dict:
        dict[char]+=1
print("Number of vowels present in a string is : ",dict)




