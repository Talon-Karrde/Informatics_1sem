import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

f = open('iris_data.csv')
df = pd.read_csv('iris_data.csv')
fig = plt.figure(figsize = (4,16),dpi=100 )
#положение
ax1 = fig.add_subplot(321) 
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323) 
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325) 
ax6 = fig.add_subplot(326)

ax1.plot(df['SepalLengthCm'],df['SepalWidthCm'],'r.' )
ax1.set_xlabel('SepalLengthCm')
ax1.set_ylabel('SepalWidthCm')

ax2.plot(df['SepalLengthCm'],df['PetalLengthCm'],'r.' )
ax2.set_xlabel('SepalLengthCm')
ax2.set_ylabel('PetalLengthCm')

ax3.plot(df['SepalLengthCm'],df['PetalWidthCm'],'r.' )
ax3.set_xlabel('SepalLengthCm')
ax3.set_ylabel('PetalWidthCm')

ax4.plot(df['SepalWidthCm'],df['PetalLengthCm'],'r.' )
ax4.set_xlabel('SepalWidthCm')
ax4.set_ylabel('PetalLengthCm')

ax5.plot(df['SepalWidthCm'],df['PetalWidthCm'],'r.' )
ax5.set_xlabel('SepalWidthCm')
ax5.set_ylabel('PetalWidthCm')

#вычисление коэффициентов
pr=df['PetalLengthCm']*df['PetalWidthCm'] #xy
t=0
for line in df['PetalLengthCm']:
     t+=1 #число этих штук
sq=0
for line in pr:
    sq=sq+float(line)
spr=sq/t  #ср(xy) 
sw=0
for line in df['PetalLengthCm']:
    sw=sw+float(line)
sx=sw/t   #срx
se=0
for line in df['PetalWidthCm']:
    se=se+float(line)
sy=se/t   #срy
kv=df['PetalLengthCm']*df['PetalLengthCm'] #x*x
sr=0
for line in kv:
    sr=sr+float(line)
sxx=sr/t  #ср(x*x)
a=(spr-(sx*sy))/(sxx-(sx*sx))
b=sy-a*sx
print('a6=',a)
print('b6=',b)

#a,b - коэфы для прямой

ax6.plot(df['PetalLengthCm'],df['PetalWidthCm'],'r.' )
x = np.linspace(1,8,100)
y = a*x+b
ax6.plot(x,y);
ax6.set_xlabel('PetalLengthCm')
ax6.set_ylabel('PetalWidthCm')

fig.show()



#SepalLengthCm
#PetalLengthCm
#PetalLengthCm
#PetalWidthCm
