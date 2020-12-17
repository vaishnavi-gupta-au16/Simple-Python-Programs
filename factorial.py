"""
Q1. Write a program to find the factorial of a number.
Eg 5! = 120 ( 5 * 4 * 3 * 2 * 1)
"""
print("Factorial")
print("Enter the number you want the print")
user_input = int(input())
fact = 1
for i in range (1,user_input+1):
    print(i)
    fact = fact * i
print(fact)
      