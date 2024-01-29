# def getEmpData(emp1,emp2):
#     print("Employee 1: ",emp1)
#     print("Employee 2: ",emp2)


# getEmpData("ram","shyam","ajay")    

#*args

# def getEmpData(a,*args,x):
#     print("a -->",a)
#     print("args -->",args)
#     print("type ",type(args))
#     print("x -->",x)


# getEmpData("ram","shyam","ajay",x=100)    
#getEmpData()    

def getEmpData(a,*args,**kwargs):
    print("kwargs",kwargs)
    print("a -->",a)
    print("args -->",args)
    print("type ",type(args))
    #print("x -->",x)


getEmpData("ram","shyam","ajay",x=100,y=200,z=300,city="ayodhya")    
