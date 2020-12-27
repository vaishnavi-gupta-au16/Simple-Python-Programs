"""
Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether
that number is present in list or not. ( Iterate over list using while loop ).
"""

i = 10
mylist = []
while i > 0 :
    print("Enter the integers")
    num = input ()
    mylist.append(num)
    i = i - 1 
print("Enter no")
n = input()
i = 9
count = 0
while i >= 0:
    if n == mylist[i]:
        print ("Yes")
        count = count + 1
    i = i - 1
if count == 0:
    print("No")

if n in mylist:
    print("yes")
else:
    print("no")


