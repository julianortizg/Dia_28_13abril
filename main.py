import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import math

my_dict=open('texto.txt')
my_dict=eval(my_dict.readline())
#print ("Clave:",k,"Valor:",v)

myList = my_dict.items()
myList = sorted(myList) 
x, y = zip(*myList) 

plt.plot(x, y)
plt.show()