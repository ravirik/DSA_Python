def print_numberop(n):
    if(n<1):
        return 0
    print(n)
    print_numberop(n-1)

n=int(input('Enter a number : '))
print_numberop(n)
