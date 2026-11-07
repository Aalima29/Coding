user=input("Enter a String")
punchuation="+-()*&^%$#@!?;:.,[]{}/<>"
empty_str=""

for i in user:

 if i not in punchuation:
    empty_str+=i
print(empty_str)