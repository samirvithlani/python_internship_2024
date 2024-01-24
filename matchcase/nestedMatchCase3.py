gender = input("enter your gender :")

match gender:
    
    case "MALE" | "male" | "m":
        print("Male...")
        age = int(input("Enter your age: "))
        
        match age:
            case age if age >= 18:
                print("You are eligible for medical insurance")
            case _:
                print("You are not eligible for medical insurance")    
        
    case "FEMALE" | "female" | "f":
        print("Female..")    
        