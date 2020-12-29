"""
Find largest and smallest elements of a list.
"""

def largest_and_smallest(list1):
    largest = 0
    for i in range (0,len(list1)):
        if largest < list1[i]:
            largest = list1[i]
    return largest

print(largest_and_smallest([7,8,2,22,0,4,5]))
