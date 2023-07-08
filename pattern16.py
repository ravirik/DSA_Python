def pattern16(n):
    for i in range(1, n+1):
        print(chr(ord('A')+i-1) * i)

n = int(input("Enter a number: "))
pattern16(n)

