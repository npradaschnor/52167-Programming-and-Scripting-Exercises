# Noa P Prada Schnor W2 Exercise
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

#My name is Noa, then the first and last letter of my name give the number 15 (N+A = 15). The 15th Fibonacci number is 610. 
name = "Schnor"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#ord() returns an integer representing the code of the character. 
#It uses as a reference The American Standard Code for Information Interchange (ASCII code). 
#For example, the capital letter S is ASCII 83 and the lower case r is ASCII 114. 
#I found out that if I want to get the capital letter S I should press alt+83 and then after I stop pressing alt I will get a "S".
