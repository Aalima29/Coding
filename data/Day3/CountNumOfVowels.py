a="Aalima Quosar Is a Freash Graduadate"
vowels="aeiou"
a=a.casefold()
dict={}.fromkeys(vowels,0)

for char in a:
    if char in dict:
        dict[char]+=1
print(dict)