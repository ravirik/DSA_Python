def pattern5(n):
    for i in range(n):
        for j in range(i,n):
            print("* ", end = ' ')
        print("\r")

n = int (10)
pattern5(n)