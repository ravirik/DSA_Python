def pattern13(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=' ')
            num += 1
        print("\r")

n=int(input())
pattern13(n)