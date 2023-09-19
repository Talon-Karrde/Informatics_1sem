array = [int(a) for a in input().split()]
for i in range(len(array)):
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            break
    else:
        print(array[i], end=' ')
