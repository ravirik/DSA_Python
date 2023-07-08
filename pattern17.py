def pattern17(n):
    for i in range(0,n):
        for j in range(n-i-1):
            print(' ',end='')
        breakpoint = (2*i+1)//2
        ch ='A'
        for j in range(1,2*i+1):
            print(ch,end='')
            if j<=breakpoint:
                ch=chr(ord(ch)+1)
            else:
                 ch=chr(ord(ch)-1)
        for j in range(n-i-1):
            print(' ',end='')
        print("\r")

n= int(input())
pattern17(n)