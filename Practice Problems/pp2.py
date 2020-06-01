apples = int(input("Enter the number of apples\n"))
mx = int(input("Enter the minimum number to check\n"))
mn = int(input("Enter the maximum number to check\n"))

for i in range(mx, mn+1):
    if apples%i==0:
        print(f"{i} is a divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")
