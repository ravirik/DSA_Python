def pattern20(n):
    for i in range(0,2*n-1):
        if i<n:
            for j in range(0,i+1):
                print('*',end=' ')
            for j in range(0,2*(n-i-1)):
                print(' ',end=' ')
            for j in range(0,i+1):
                print('*',end=' ')
            print("\r")
        if i>=n:
            for j in range(0,2*n-i-1):
                print('*',end=' ')
            for j in range(0,2*(i-n+1)):
                print(' ',end=' ')
            for j in range(0,2*n-i-1):
                print('*',end=' ')
            print("\r")

n=int(input('Enter a number:'))
pattern20(n)
