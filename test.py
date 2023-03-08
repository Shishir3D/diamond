n = 6
for i in range(n):
    left_space = " " * (n-i-1)
    middle_space = " " * (i*2+1)
    print(left_space + "*" + middle_space + "*")
for i in range(n-2, -1, -1):
    left_space = " " * (n-i-1)
    middle_space = " " * (i*2+1)
    print(left_space + "*" + middle_space + "*")