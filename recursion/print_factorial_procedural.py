def print_factorial_procedural(i,cnt=1):
    if(i<1):
        print(cnt)
        return
    print_factorial_procedural(i-1,cnt*i)

n=int(input('Enter a number : '))
print_factorial_procedural(n)