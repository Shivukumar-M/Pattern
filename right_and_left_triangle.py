# Right-Angled Triangle Pattern
number=int(input("Enter The Number : "))
print("Right-Angled Triangle Pattern")
for i in range(1,number+1):
    print('*' *i)
   
print()

# Left-Angled Triangle Pattern
print("Left-Angled Triangle Pattern")
for i in range(1,number+1):
    print(' ' *(number-i) + '*' * i)
   

