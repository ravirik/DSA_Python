def print_divisors(n):
    for i in range(1,n):
        if (n%i ==0):
            print(i ,end =' ')
    print('\r')

n=int(input('Enter a number : '))
print_divisors(n)