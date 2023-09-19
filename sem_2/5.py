array1 = [int(a) for a in input().split()]
array2 = array1.pop()
array1 = [array2] + array1
for i in range(len(array1)):
    print(array1[i], end = ' ')
