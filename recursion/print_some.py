
cnt=0
def print_some(n):
    global cnt
    if(cnt<n):
        print(cnt)
        cnt+=1
        print_some(n)
    else:
        return 0


n = int(input('Enter a number : '))
print_some(n)