n = 6
leftspace,middlespace,rightastrick = n,0,0
for i in range((n*2)-1):
    if i < n:
        print(" " * leftspace + "*" + " " * middlespace + "*" * rightastrick)
        if i == 0:
            middlespace = -1
            rightastrick = 1
        if i < (n-1):
            leftspace = leftspace - 1
            middlespace = middlespace + 2
    else:
        leftspace = leftspace + 1
        middlespace = middlespace - 2
        if i == ((n*2)-2):
            rightastrick = 0
        print(" " * leftspace + "*" + " " * middlespace + "*" * rightastrick)