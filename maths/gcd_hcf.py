def gcd_hcf(n1,n2):
    gcd = 0
    for i in range(1,min(n1,n2)+1):
        if(n1%i==0 and n2%i==0):
            gcd = i
    print(gcd)

n1= int(input('Enter a number : '))
n2= int(input('Enter a number : '))

gcd_hcf(n1,n2)