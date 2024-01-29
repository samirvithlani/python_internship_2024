class Area:
    
    def __init__(self,lenght,breadth):
        print("lenght = ",lenght)
        print("breadth = ",breadth)
        self.h = lenght
        self.b = breadth
        print("Hello from Area constructor")
    
    def squareArea(self):
        print("Hello from squareArea")
        return self.h * self.b    
    

a = Area(10,20)
ans = a.squareArea()        
print("ans = ",ans)