# Take 10 integer inputs from user and store them in a list and print them on screen using function.


num = []
def store_variable():
    n = int(input("enter the 10 integer inputs"))
    for i in range(0,n):
        a = int(input())
        num.append(a)

    print(num)

store_variable()
 
## other solution ##
 
# i = 1
# lst = []
# print("enter the digits you want to store")
# while i <= 10:
#     num = int(input())
#     lst.append(num)
#     i = i+1
# print(lst)

