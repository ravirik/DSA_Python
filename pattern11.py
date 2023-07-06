def pattern11(n):
    start = int(n)
    for i in range(n):
        if (i%2==0):
            start=0
        else:
            start=1
        for j in range (0,i+1):
            print(start,end= ' ')
            start =1-start
        
        print("\r")

n = int(input())
pattern11(n)