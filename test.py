def print_some(i,cnt=0):
    if(i<1):
        print(cnt)
        return
    print_some(i-1,cnt+i)


n = int(input('Enter a number : '))
print_some(n)