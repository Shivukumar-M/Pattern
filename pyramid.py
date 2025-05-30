# Pyramid Pattern
number=int(input("Enter The Number : "))
print("Pyramid Pattern")
for i in range(1,number+1):
    print(' ' * (number-i) + '*' *( 2*i-1) )

# Inverted Pyramid Pattern
print("Inverted Pyramid Pattern")
for i in range(number,0,-1):
    print(' '*(number-i) + '*' *( 2* i -1))