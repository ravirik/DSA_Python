def print_fibonacci_number(n):
    if n<=1:
        return n
    first=print_fibonacci_number(n-1)
    last=print_fibonacci_number(n-2)
    return first+last

n=int(input("Enter a number : "))
print(print_fibonacci_number(n))