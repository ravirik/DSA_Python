def reverse_num(n):
    rev_num=0
    while(n>0):
        last_dig=n%10
        rev_num=(rev_num*10)+last_dig
        n = n//10
    print(rev_num,end =' ')

n= 123456789123456789123456789123456789
reverse_num(n)