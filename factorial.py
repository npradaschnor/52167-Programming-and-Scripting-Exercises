#Noa P Prada Schnor 2018-03-05

#option 1
def factorial(i):
    number = 1 #number is the result
    while i >= 1: #i is the positive integer that it will return its factorial.While the positive integer is =1
        number = number * i #result is the number multiplied by the positive integer
        i = i - 1 #the positive integer should be minus 1
    return number #return number and continue the loop while i is equal 1, then stop the loop
print(factorial(5))
print(factorial(7))
print(factorial(10))

#option 2
def factorial(integer): #positive integer that will return its factorial
    if integer < 2: #if integer is less than 2
        return 1 #consider integer as 1
    return integer * factorial(integer - 1) #return the positive integer multiplying by itself -1
print(factorial(5))
print(factorial(7))
print(factorial(10))

#shortcut
from math import factorial #shortcut with no need to create a defining function
print(factorial(5))
print(factorial(7))
print(factorial(10))
