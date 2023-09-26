def print_numbersum_functional(n):
    if(n==1):
        return 1
    return n + print_numbersum_functional(n-1)


n=int(input('Enter a number : '))
print(print_numbersum_functional(n))