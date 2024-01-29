class Student:
    
    name = "amit" # class variable / static variable /only one copy will generate
    #instance variable copy will generate for each object
    
    def getStudentData(self):
        #self stu
        print("Hello from getStudentData")
        self.age = 20 # instance variable
        address ="delhi" #local variable
        print("address",address)
        #print("self",self)
    
    def printStudentData(self):
        print("age",self.age)    
        #print("name",address)
        
        

#stu is an object of Student class
stu = Student()        
stu.getStudentData() # Student.getStudentData(stu)
#print("stu",stu)
print("name = ",Student.name)
print("name = ",stu.name)
stu.printStudentData()