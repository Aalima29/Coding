# # convert number to string
# a=[10,20,30]
# result=list(map(str,a))
# print(result)

# # convert string into integer
# a=['10','20','30','40']
# result=list(map(int,a))
# print(result)

# Add 5 to every num

# a=[10,20,30,40]
# result=list(map(lambda x:x+5,a))
# print(result)

# filters

# Numbers greater than 10
# a=[1,5,20,30,50]
# result=filter(lambda x:x>10,a)
# print(list(result))

# odd numbers
# a=[1,5,20,30,50]
# result=filter(lambda x:x%2!=0,a)
# print(list(result))

# positive num
# a=[-1,5,-20,30,50]
# result=filter(lambda x:x>0,a)
# print(list(result))


# fitering with strings
# names = ["Aman", "Ali", "Bob", "Ankit", "John"]
# result=list(filter(lambda name:name.startswith("A"),names))
# print(result)

# reduce
# sum 
# from functools import reduce
# a=[1,2,3,4,5,6]
# Result=reduce(lambda x,y:max(x,y),a)
# print(Result)

a=[1,2,3]
b=a
print(a==b)
print(a is b)