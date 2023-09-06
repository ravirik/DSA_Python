def print_namen(n,cnt=0):
    if(cnt<n):
        print('Ravi')
        print_namen(n,cnt+1)
    else:
        return 0

n=int(input('Enter a number : '))
print_namen(n)