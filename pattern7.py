def pattern7(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(' ', end=' ')
        for j in range(0,2*i+1):
            print("*", end=' ')
        for j in range(0,n-i-1):
            print(' ',end=' ')
        print("\r")

n = int (10)

pattern7(n)