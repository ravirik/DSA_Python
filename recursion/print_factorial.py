def print_factorial(n):
    if(n<1):
        return 1
    return n*print_factorial(n-1)

n=int(input('Enter a number : '))
print(print_factorial(n))