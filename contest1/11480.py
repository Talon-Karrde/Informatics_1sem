n=int(input())
m=list(map(int, input().split()))
l = m[:]
for i in range(n - 2, -1, -1):#с конца ищем максимумы
    if m[i]<l[i+1]:
        l[i] = l[i + 1]
    else:
        l[i]=m[i]
r = 0
for i in range(n):
   r = r + l[i] - m[i]
print(r)
