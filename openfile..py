 #Noa P Prada Schnor  2018-02-28
 #Adapted from Mohamed Noor
 
 with open("data/iris.csv", 'r') as f:
  for line in f:
    line = line.replace(',', ' ') #returns a copy of the string in which the occurrences of old (',') have been replaced with new('')
    line = line.rstrip() #strings are immutable, so creates a new string instance with the stripped content
    print(line[:16].strip()) #strip - returns a copy of the string in which all chars have been stripped from the beginning and the end of the string
