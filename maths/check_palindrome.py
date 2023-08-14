def check_palindrome(n):
    check_num = n
    rev_num = 0
    while(n>0):
        last_dig = n%10
        rev_num=(rev_num*10)+last_dig
        n=n//10
    if (check_num ==rev_num):
        print("True")
    else:
        print("False")

n= int(input('Enter a number : '))
check_palindrome(n)