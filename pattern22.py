def pattern22(n):
    for i in range(0,2*n-1):
        for j in range(0,2*n-1):
            top=i
            left=j
            right=(2*n-2)-j
            down=(2*n-2)-i
            distance= n-(min(min(top,down),min(left,right)))
            print(distance,end=' ')
        print("\r")

n= int(input('Enter a number:'))
pattern22(n)

