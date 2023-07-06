def pattern7(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(' ', end=' ')
        for j in range(0,2*i+1):
            print("*", end=' ')
        for j in range(0,n-i-1):
            print(' ',end=' ')
        print("\r")

def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end= ' ')
        for j in range(0,2*n-(2*i+1)):
            print("*", end= ' ')
        for j in range(i):
            print(" ", end=' ')
        print("\r")

n = int(input());
pattern7(n)
pattern8(n)