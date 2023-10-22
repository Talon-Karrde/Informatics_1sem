d = list(map(int, input().split()))
size=len(d)
din=[0]*len(d)

if size > 0:
    din[0] = d[0]
if size > 1:
    din[1] = max(d[0], d[1])
    
for i in range(2, len(d)):
    din[i] = max(din[i-1],d[i] + din[i-2])
    
print(din[size-1])
