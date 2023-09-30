import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
fig = plt.figure(figsize = (1,1)) 
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

z=0
q=0
e=0
f = open('Y.txt')
for line in f:
    if float(line)>= 1.5:
        z+=1
    elif float(line)>1.2 and float(line)<1.5:
        q+=1
    elif float(line)<=1.2:
        e+=1

a=z/(z+q+e)
b=q/(z+q+e)
c=e/(z+q+e)

ax1.pie([0.3, 0.3, 0.3], labels = ['Iris-virginica','Iris-versicolor','Iris-setosa'])
ax2.pie([a, b, c], labels = ["больше 1.5см",'больше 1.2см и меньше 1.5см','меньше 1.2см'])
fig.show()

