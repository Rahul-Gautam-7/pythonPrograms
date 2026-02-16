#factorial program
import math


def fact(nums):
    factorial=1
    while(nums > 0):
        factorial *= nums
        nums= nums -1
    return factorial



nums = int(input('Enter a number'))
if nums:
    print(fact(nums))
    print(math.factorial(nums))