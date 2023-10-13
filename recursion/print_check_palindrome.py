def print_check_palindrome(i,arr,n):
    if i>=n/2:
        return True
    if arr[i]!=a[n-i-1]:
        return False
    return print_check_palindrome(i+1,arr,n)

a=input()
n=len(a)
if print_check_palindrome(0,a,n):
    print("It's a palindrome")
else:
    print("It's not a palindrome")