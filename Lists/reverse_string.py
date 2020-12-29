"""
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in 
another list but in reverse order.
"""
first = []
print("enter 10 integer ")
for i in range(0,10): 
    num = int(input())
    first.append(num)

print(first)
second = first[::-1]
print(second)
    