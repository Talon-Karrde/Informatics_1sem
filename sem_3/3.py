Pr=list(map(int,input().split()))
a=Pr[0]
b=Pr[1]

def nod(a,b):
    while a!=0 and b!=0:
        if a>=b:
            a=a-b
        else:
            b=b-a
    return a or b

d=nod(a,b)
c=max(a,b)
min=2*c+1
x=2*c
y=2*c
for i in range(-c, c):
    for j in range(-c, c):
        if i*a+j*b==d:
            if (abs(i)+abs(j))<min: #типа модуль
                min=abs(i)+abs(j)
                x=i
                y=j
            if (abs(i)+abs(j))==min:
                if i<x:
                    x=i
                    y=j   
print(x,y,d)
            
        

