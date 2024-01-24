no1 =0
no2 =1

print(no1,end=" ")
print(no2,end=" ")
add = 0
# 0 1
for i in range(1,10):
    #  0 + 1 = 1
    #  1 + 1 = 2
    #  1 + 2 = 3 
    #  2 + 3 = 5
    add = no1 + no2
    print(add,end=" ") # 1 2 3
    no1 = no2 #no1 = 1, no1 = 1, no1 = 2
    no2 = add # no2 = 1, no2 = 2, no2 = 3