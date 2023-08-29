def pattern18(n):
    for i in range(n):
        for ch in range(ord('E')-i,ord('E')+1):
            print(chr(ch),end=' ')
        print("\r")

n=int(input('Please enter input value:'))
pattern18(n)