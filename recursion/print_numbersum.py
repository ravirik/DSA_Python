def print_numbersum(i,cnt=0):
    if(i<1):
        print(cnt)
        return
    print_numbersum(i-1,cnt+i)

n=int(input('Enter a number : '))
print_numbersum(n)