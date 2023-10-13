def print_reverse_array(arr,i,n):
    if i>=n/2:
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    print_reverse_array(arr,i+1,n)

a=[]
n=int(input('Enter a number : '))
for j in range(0,n):
    alt=int(input())
    a.append(alt)
print(a)
print_reverse_array(a,0,n)
print(a)