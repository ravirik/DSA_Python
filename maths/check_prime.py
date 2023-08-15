def check_prime(n):
    cnt = 0
    for i in range(1,n+1):
        if(n%i ==0):
            cnt += 1
    if(cnt<=2):
        print(n,' is a prime number')
    else:
        print(n,' is not a prime number')

n=int(input('Enter a number : '))
check_prime(n)