def printData() ->None:
    print("Hello World")
    #without return  without parameter

printData()    


def add(a,b)->int:
    #with return with parameter
    #c = a+b
    return a+b
    #return c

ans = add(10.20,20)    
print("ans -->",ans)


#users.. list
def printAllUsers(users):
    for i in users:
        print(i)

printAllUsers(["ram","shyam","mohan"])        
    