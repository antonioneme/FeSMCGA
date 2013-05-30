import   sys, math, mif, random
#from numpy import genfromtxt

def   read_data(file):
   f = open(file, "r")
   x = f.readlines()
   f.close()
   Classes = []
   D = []
   for i in range(len(x)):
      xx = x[i].split(' ')
      tmp = []
      for j in range(len(xx) - 1):
         tmp.append(float(xx[j]))
      D.append(tmp)
      Classes.append(int(xx[len(xx) - 1]) )
   #D2 = transpose(D)
   #return [D2, Classes]
   return [D, Classes]
