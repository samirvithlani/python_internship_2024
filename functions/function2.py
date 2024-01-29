#keyword args

def getUserData(name,email,age):
    print("Name: ",name)
    print("Email: ",email)
    print("Age: ",age)



#getUserData("Ram","ram@gmail.com",23)   
#getUserData("ram@gmail.com",23,"ram")   
getUserData(age=23,email="ram@gmail.com",name="Ram")