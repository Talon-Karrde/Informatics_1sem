A=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]
B=[2, 4, 6, 8, 10, 12, 10, 6, 5, 5, 1]
ax=set(A)
bx=set(B)
f=set() #для А
f1=set()
for a in A:
    if a in f1:
        continue
    if a in f:
        f.remove(a)
        f1.add(a)
    else:
        f.add(a)
z=set()  #для В
z1=set()
for b in B:
    if b in z1:
        continue
    if b in z:
        z.remove(b)
        z1.add(b)
    else:
        z.add(b)
x=set()  #для объединения А и В
x1=set()
for c in (A+B):
    if c in x1:
        continue
    if c in x:
        x.remove(c)
        x1.add(c)
    else:
        x.add(c)
print("A: ",A)
print("B: ",B)
print("уникальные из А:  ",list(f))
print("уникальные из B:  ",list(z))
print("уникальные из объединения:  ", list(x))
print("Содержащиеся в обоих списках:  ",list(ax&bx))
