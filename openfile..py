#Noa P Prada Schnor  2018-02-28
#Adapted from Mohamed Noor
 
with open("data/iris.csv", 'r') as f:
  for line in f:
    line = line.replace(',', ' ') #returns a copy of the string in which the occurrences of old (',') have been replaced with new('')
    line = line.rstrip() #strings are immutable, so creates a new string instance with the stripped content
    print('{0[0]:1} {0[1]:1} {0[2]:1} {0[3]:1} {0[4]:1} {0[5]:1} {0[6]:1} {0[7]:1} {0[8]:1} {0[9]:1} {0[10]:1} {0[11]:1} {0[12]:1} {0[13]:1} {0[14]:1} {0[15]:1}'.format(line))
