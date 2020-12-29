"""
Write a program to find the product of all elements of a list.
"""

def product_of_elements_of_list(list1):
    mul = 1
    for i in range(0,len(list1)):
        mul = mul * list1[i]

    return mul

print(product_of_elements_of_list([1,2,3,4,5]))
