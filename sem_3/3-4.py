size=int(input())
symb=input()
def t(size, symb):
    for i in range(1, int((size-1)/2+2)):
        print(i*symb)
    for i in range(int((size-1)/2+2), size+1):
        print(symb*(size-i+1))
t(size, symb)
        
