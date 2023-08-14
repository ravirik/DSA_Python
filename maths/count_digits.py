def count_digits(n):
    coun_t=0
    while(n>0):
        n=int(n/10)
        coun_t += 1
    print(coun_t)

n=int(input('Enter a number : '))
count_digits(n)