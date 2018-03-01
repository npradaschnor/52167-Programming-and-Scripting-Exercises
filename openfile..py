#Noa P Prada Schnor  2018-02-28

import csv

with open('data/iris.csv', newline='') as csvFile:
  for line in csvFile:
    line = line.replace(',', ' ')
    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15])
