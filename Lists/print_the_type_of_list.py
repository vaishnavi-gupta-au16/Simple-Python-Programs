"""
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s.
"""
a = []
print("enter the  10 integer")
for i in range(1,11):
    num = int(input())
    a.append(num)
even = 0
odd = 0
zero = 0
positive = 0
negative = 0

for i in range(0,len(a)):
    if a[i] > 0:
        positive += 1

    if a[i] < 0:
        negative += 1

    if a[i] % 2 == 0 and a[i] != 0:
        even = even + 1

    if a[i] % 2 != 0:
        odd = odd + 1 

    if a[i] == 0:
        zero = zero +1
    
print("even no =", even, "odd no =", odd , "zero no =", zero, "positive no =", positive, "negative no =", negative)
