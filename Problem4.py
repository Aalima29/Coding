# Write a Python program to translate a message into a Secret Code Language.

# Use the following rules to translate normal English into the secret code language.

# 🔐 Coding Rules

# For each word:

# If the word contains at least 3 characters:

# Remove the first letter.
# Append that first letter to the end.
# Add three random characters at the beginning.
# Add three random characters at the end.

# Else (word has fewer than 3 characters):

# Simply reverse the word.
# 🔓 Decoding Rules

# For each coded word:

# If the original word contains less than 3 characters:

# Simply reverse the coded word.

# Else:

# Remove the 3 random characters from the beginning and end.
# Remove the last letter.
# Append that removed letter to the beginning.

# ------------------------encoding-----------------------------------
import random
import string
word="hello"

if len(word)>=3:
    random_start=""
    random_end=""
    for i in range(1,4):
      character=random.choice(string.ascii_letters)
      random_start=random_start+character
    for i in range(3):
       character=random.choice(string.ascii_letters)
       random_end=random_end+character
    
    

    First=word[0]
    new_word=word[1:]
    result=new_word+First
    final=random_start+result+random_end
    
    
# ---------------------decoding---------------------------------------------
    coded_word=final
    if len(coded_word)>=3:
       
       decoded=coded_word[3:-3]
       print(decoded)
       last=decoded[-1]
       rem=decoded[-1]
       result=last+rem

    
    
       print(result)

    


    else: 

    
    
      print("Decoded:", coded_word[::-1])
    
