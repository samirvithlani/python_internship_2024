

'''
    for(int i=0;i<10;i++)
'''
# for i in range(10):
# for i in range(1,11):
# for i in range(1,20,2):
#     print(i)


# for i in range(10,0,-1):
#     print(i)

no = int(input("Enter no: "))
add = 0

for i in range(1,no+1):
    if i % 2==0:
        add+=i
    print(i)
        
    #add = add + i

print("Addition is",add)    
