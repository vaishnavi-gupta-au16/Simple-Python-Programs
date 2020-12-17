"""
Take input of age of 3 people by user and determine oldest and youngest among them.
12 10 9
"""
print("Enter the Age of First Person")
First=int(input())
print("Enter the Age of Second Person")
Second=int(input())
print("Enter the Age of Third Person")
Third=int(input())

if(First > Second and First > Third):
    print("First age is greater that is ", First)
elif (Second > Third ):
    print("Second is greater that is", Second)
else:
    print("Third is greater that is", Third)
