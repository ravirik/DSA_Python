def gcd_hcf_2(a,b):
    while(a>0 and b>0):
        if (a>b):
            a=a%b
        else:
            b=b%a
    if(a==0):
        print(b)
    else:
        print(a)

a = int(input('Enter a number : '))

b = int(input('Enter a number : '))

gcd_hcf_2(a,b)

