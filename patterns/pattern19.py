def pattern19(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end=' ')
        for j in range(2*i):
            print(' ',end=' ')
        for j in range(n-i):
            print('*',end=' ')
        print("\r")
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        for j in range(2*(n-i-1)):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
        print("\r")

n=int(input('Enter a number:'))
pattern19(n)