#153 370 371..
'''
    1 + 125 + 27 = 153

'''

no = int(input("Enter a number: "))
temp = no
noofdigits = 0

while temp>0:
    temp = temp//10
    noofdigits+=1
    

    
print(noofdigits)


add =0
rem =0
while no>0:
    rem = no%10
    add = add + rem**noofdigits
    no = no//10

print(add)    
