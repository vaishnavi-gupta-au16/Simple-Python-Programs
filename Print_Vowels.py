# """
# Q1. Write a program to print the vowels in a particular str given by user.

# Eg Attainu
# Output: vowels are A, a, i, u

vowels = ['A','a','E','e','I','i','O','o','U','u']
print("Please input some String ")
user_input = input()
for i in user_input:
    if i in vowels:
        print(i)
        continue
print("Program End")   