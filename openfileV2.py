#Noa P Prada Schnor 2018-02-28

with open("data/iris.csv") as f:
  for line in f:
    numerical = line.split(',')  # Splits the string whenever it sees a space character
    print('{0[0]:10} {0[1]:10} {0[2]:10} {0[3]:10}'.format(numerical)) #Accessing arguments’ items. Example: 
    # coord = (3, 5)
    # 'X: {0[0]};  Y: {0[1]}'.format(coord)
    # 'X: 3;  Y: 5'

  
  #Noa P Prada Schnor 2018-03-07
  
  Def makefloat(teststr): #Gerhard Van Der Linde def Function string to number
  try:
    return float(teststr)  # return a floating point value if possibe.
  except:
    return teststr  # otherwise return the string as is


with open("data/iris.csv") as data:
  makefloat(data)
  for line in data:
    line = line.split(',')
    print('{0:10} {0:10} {0:10} {0:10}'.format(line[0], line[1], line[2], line[3]))
