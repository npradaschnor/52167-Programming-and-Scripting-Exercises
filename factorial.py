#Noa P Prada Schnor 2018-03-05

def factorial(i):
    number = 1
    while i >= 1:
        number = number * i
        i = i - 1
    return number
print(factorial(5))
print(factorial(7))
print(factorial(10))

from math import factorial
print(factorial(5))
print(factorial(7))
print(factorial(10))


def factorial(integer):
    if integer < 2:
        return 1
    return integer * factorial(integer - 1)
print(factorial(5))
print(factorial(7))
print(factorial(10))
