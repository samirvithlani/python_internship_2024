#123 --> 3
# 123 // 10 = 12
# 12 // 10 = 1
# 1 // 10 = 0

#67890 --> 5
# 67890 // 10 = 6789
# 6789 // 10 = 678
# 678 // 10 = 67
# 67 // 10 = 6
# 6 // 10 = 0

no = int(input("Enter a number: ")) #123
count = 0
while no>0:
    no = no // 10
    count+=1

print("Total digits are",count)    
