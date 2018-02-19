#Noa P Prada Schnor, 2018-02-19
#Project Euler Problem 5 (https://projecteuler.net/problem=5)

i = range(1,21) #"list" from 1 to 20
f = 0 #number that I need to find out

while i <= 20: #while the number of my created list is <=20
  if f % i == 0: #f must be an even number
  f = f + 1 #every time the loop happens it must increase the number that I need to find out

  print(f) #smallest positive number that is evenly divisible by all of the numbers from 1 to 20
