#Noa P Prada Schnor, 2018-02-19, modified 2018-03-03
#Project Euler Problem 5 (https://projecteuler.net/problem=5)

i = 2 #number starts from 2
f = 2 #number that I need to find out

while i < 21: #while the number is 20
  if f % i == 0: #f must be an even number
   i = i + 1 #add 1 to the number
  else: #otherwise
    f=f+1 #add a number to the number I need to find out
    i=2

print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:',f) 
