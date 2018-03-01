#Noa P Prada Schnor  2018-03-01
#Print decimal places aligned, with a space between the columns

import csv

with open('data/iris.csv', newline='') as csvFile:
  for line in csvFile:
    line = line.replace(',', ' ') #no comma separating the numbers
    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15]) #print an output splitting the line and adding space between them
