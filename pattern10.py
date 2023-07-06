def pattern10(n):
    for i in range(1,2*n-1):
        stars = int(i)
        if i > n:
            stars = 2*n-i
        for j in range(1,stars):
            print('*', end =' ')
        print("\r")

n= int(input())
pattern10(n)