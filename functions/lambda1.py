#anno function

# def printData():
#     print("Hello World")

x = lambda : print("Hello World")
x()

x1 = lambda no1,no2 : print("no1 = ",no1,"no2 = ",no2)
x1(20,30)

add = lambda a,b,c : a+b+c
ans = add(10,20,30)
print("Ans = ",ans)


isPalindrome = lambda name: True if name == name[::1] else False

flag = isPalindrome("nitin")
print("Flag = ",flag)
    
findBigger = lambda a,b : a if a > b else b
print("Bigger Number is ",findBigger(10,20))    