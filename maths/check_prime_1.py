import math

def check_prime_1(n):
    cnt = 0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i ==0):
            cnt += 1
            if(n//i != i):
                cnt += 1
    if(cnt <= 2):
        print(n,' is a prime number')
    else:
        print(n,' is not a prime number')
    print('\r')

n=int(input('Enter a number : '))
check_prime_1(n)
