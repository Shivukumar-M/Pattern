# Inverted-Right-Angled Triangle Pattern
number=int(input("Enter The Number : "))
print("Inverted-Right-Angled Triangle Pattern")
for i in range(number,0,-1):
    print('*'*i)
   
# Inverted-Right-Angled Triangle Pattern
print("Inverted-left-Angled Triangle Pattern")
for i in range(1,number+1):
    print(' ' * i + "*" * ((number+1)-i))
   