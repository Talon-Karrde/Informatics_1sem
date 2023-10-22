def sim(n, m):
    if n==0 or m==0:
        return 0
    elif n % 2 == 0 or m % 2 == 0:#нет центра при таких значениях
        return 0
    return 4*sim(n // 2, m // 2)+1 
 
n, m = map(int,input().split())
mini = sim(n, m)
print(mini)
