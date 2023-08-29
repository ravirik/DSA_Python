def pattern6(n):
    for i in range(1,n):
        for j in range(i,n-1):
            print(j-i+1, end = ' ')
        print("\r")
    
n = int (10)

pattern6(n)