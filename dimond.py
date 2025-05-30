#Diamond Pattern
number=int(input("Enter The Number : "))
for i in range(1,number):
    print(' ' *(number-i)+ '*' * (2*i-1))
for i in range(number,0,-1):
    print(' ' *(number-i)+ '*' * (2*i-1))
