"""
Write a program to print sum, average of all numbers, smallest and largest element of a list.
"""
# def test_me(list1):
#     sum = 0
#     avg = 0
 
#     largest = 0
#     for i in range(1,len(list1)):
#         sum = sum + list1[i]

#         if list1[i] > largest:
#             largest = list1[i]
#     for i in range(1,len(list1)):
#         if list1[i] > largest:
#             smallest = list1[i]
 


#     print("largest =",largest)
#     print("smallest =",smallest)
     
#     avg = sum / len(list1)
#     print("sum", sum)
#     print("avg", avg)


# test_me([1,2,3,4,5])

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = list()
    for c in s :
        if c == "(":
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c == "{":
            stack.append(c)
        elif c == ")" and stack[-1] == "(":
            stack.pop()
        elif c == "]" and stack[-1] == "[":
            stack.pop()
        elif c == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False
            print(stack)
    if len(stack) == 0:
        return True
    return False

strr = "{}"
print(isValid(strr))