"""
Q.Take two int values from user and print greatest among them.
"""
print("enter two values for knowing which one is greater !")
print("enter first values")
First=int(input())

print("enter second values")
Second=int(input())

if (First > Second):
    print(First ,"Value is greater and", Second, "is small")
elif (Second > First):
    print(Second , "Value is greater and", First ,"is small")

else:
    print("Both are equal")

print("program is completed")

