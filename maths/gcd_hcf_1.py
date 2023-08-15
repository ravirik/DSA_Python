def gcd_hcf_1(n1,n2):
    for i in range(min(n1,n2),0,-1):
        if(n1%i==0 and n2%i==0):
            print(i)
            break

n1 = int(input('Enter a number : '))
n2 = int(input('Enter a number : '))

gcd_hcf_1(n1,n2)