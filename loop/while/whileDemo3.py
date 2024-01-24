# 123 = 123 % 10 - 3    
#123 // 10 = 12 % 10 = 2

no = int(input("Enter a number: ")) #123
rem = 0
add = 0
mul = 1
while no>0:
    rem = no % 10 # 123 % 10 = 3 12 % 10 = 2 1 % 10 = 1
    #0 + 3 = 3
    #3 + 2 = 5
    #5 + 1 = 6
    add = add + rem
    mul = mul * rem
    #123 // 10 = 12
    #12 // 10 = 1
    #1 // 10 = 0
    no = no // 10


print("Sum of digits is",add)    
print("Multiplication of digits is",mul)
    