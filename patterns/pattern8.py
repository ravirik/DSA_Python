def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end= ' ')
        for j in range(0,2*n-(2*i+1)):
            print("*", end= ' ')
        for j in range(i):
            print(" ", end=' ')
        print("\r")

n = int (10)

pattern8(n)