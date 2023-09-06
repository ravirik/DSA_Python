
def print_some(n,cnt=0):
    if(cnt<n):
        print(cnt)
        print_some(n,cnt+1)
    else:
        return 0


n = int(input('Enter a number : '))
print_some(n)