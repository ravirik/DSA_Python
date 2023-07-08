def pattern17(n):
    for i in range(0, n):
        for j in range(n - i - 1):
            print(' ', end='')
        mid_index = (2 * i + 1) // 2
        ch = 'A'
        for j in range(0, 2 * i + 1):
            print(ch,end='')
            if (j < mid_index):
                ch = chr(ord(ch)+1)
            else:
                ch = chr(ord(ch)-1)
        for j in range(n - i - 1):
            print(' ', end='')
        print("\r")

n = int(input("Enter a number: "))
pattern17(n)


