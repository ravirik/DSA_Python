def pattern2_1(n):
    for i in range(n):
        for j in range(i):
            print("* " , end = ' ' )
        print()


n=int(10)

pattern2_1(n)
