# def getStudentData(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# getStudentData(name="ram",city="ayodhya",age=23)    

def getStudentData(*args,**kwargs):
    #print("x -->",x)
    print(args)
    print(kwargs)
    print(type(kwargs))


getStudentData(100,20,30,name="ram",city="ayodhya",age=23)    