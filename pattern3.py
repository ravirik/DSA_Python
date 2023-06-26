def pattern3(n):
    for i in range(1,n):
        for j in range(1, i+1):
            print(j, end=' ')
        print("\r")

n = int(10)

pattern3(n)