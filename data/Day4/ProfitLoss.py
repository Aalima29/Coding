CP=int(input("Enter Cost Price : "))
SP=int(input("Enter Selling Price : "))
Profit=SP-CP
SP=CP+Profit
CP=SP-Profit
if SP>CP:
    print("Profit ! ")
else:
    print("Loss !")