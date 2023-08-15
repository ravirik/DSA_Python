import math

def armstrong_num(n):
    check_sum = 0
    num = n
    count = int(math.log10(n)+1)
    while(n>0):
        last_dig=n%10
        check_sum = check_sum+(last_dig**count)
        n=n//10
    if ( check_sum == num):
        print("True")
    else:
        print("False")

n = int(input('Enter a number : '))
armstrong_num(n)