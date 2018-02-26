#Noa Prada Schnor 28-02-06
#Collatz Conjecture (https://en.wikipedia.org/wiki/Collatz_conjecture)
#Week 3 Exercise

nominal = int(input("Enter integer:")) #enter a number
while nominal!=1: #while number is different from 1
    if nominal % 2 ==0: #if the previous term is even, the next term is one half the previous term
        nominal = nominal//2
        print (nominal) #Otherwise, the next term is 3 times the previous term plus 1
    else:
        nominal = (nominal * 3) + 1
        print (nominal) #The conjecture is that no matter what value of nominal, the sequence will always reach 1
