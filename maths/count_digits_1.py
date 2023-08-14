import math

def count_digits_1(n):
    count_digs = int((math.log10(n))+1)
    print(count_digs)

n=int(input('Enter a number : '))
count_digits_1(n)
