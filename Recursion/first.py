"""
Sum of all the digits of a number using recursion
"""
import math

def SumsOfDigit(n):
    sums = 0  

    sum = n % 10
    sums = sum + SumsOfDigit(n//10)
    return sums
    
print(SumsOfDigit(5432))
