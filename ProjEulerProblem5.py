#Noa P Prada Schnor, 2018-02-19
#Project Euler Problem 5 (https://projecteuler.net/problem=5)

i = 2 #number starts from 2
f = 2 #number that I need to find out

while i < 21: #while the number of my created list is <=20
  if f % i == 0: #f must be an even number
   i = i + 1
  else:
    f=f+1
    i=2

print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:',f) 
