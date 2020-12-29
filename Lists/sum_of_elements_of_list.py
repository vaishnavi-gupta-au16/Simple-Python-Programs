"""
Write a program to find the sum of all elements of a list.
"""

def sum_of_elements_of_list(list1):
    sums = 0
    for i in range(0,len(list1)):
        sums = sums + list1[i]

    return sums

print(sum_of_elements_of_list([1,2,3,4,5]))