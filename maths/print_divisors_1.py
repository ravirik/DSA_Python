import math

def print_divisors_1(n):
    ls = []
    for i in range(1,int(math.sqrt(n))+1):
        if (n%i == 0):
            ls.append(i)
            if ((n/i) != i):
                ls.append(int(n/i))
    print(sorted(ls))

n=int(input('Enter a number : '))
print_divisors_1(n)