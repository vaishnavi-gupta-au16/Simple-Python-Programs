"""
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""
print("Results are Out!! Want to Know your Grade ? \n Enter your Marks ")
user_input = int(input())

if (user_input >= 80 and user_input < 100):
    print("Congrats!!, Your Grade is A")
elif (user_input >= 60 and user_input < 80):
        print(" Great!, Your Grade is B")
elif (user_input >= 50 and user_input < 60):
        print("Work Hard!, Your Grade is C")
elif (user_input >= 45 and user_input < 50):
        print("Need to Work Hard!, Your Grade is D")
elif (user_input >= 25 and user_input < 45):
        print("Poor!, Your Grade is E")
elif (user_input <= 25):
        print("Very Poor!, You are Fail")
else:
    print("Enter Valid Marks!!")



