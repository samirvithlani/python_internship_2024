age = int(input("Enter your age: "))    


if age >=18:
    print("You are eligible to vote")
    
    if age>=21:
        print("You are eligible for marriage")
        
        if age>=60:
            print("You are eligible for senior citizen benefits")
        else:
            print("You are not eligible for senior citizen benefits")    
    else:
        print("You are not eligible for marriage")

else:
    print("You are not eligible to vote")   
    
    if age>14:
        print("You are eligible for school education")
    else:
        print("You are not eligible for school education")    
    
             