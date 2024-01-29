class Vehicle:
    
    def __init__(self):
        self.name = "car"
        self.seats = 4
        self.color = "red"
        print("Hello from Vehicle constructor")
    
    def getCarDetail(self):
        print("name = ",self.name)
        print("seats = ",self.seats)
        print("color = ",self.color)    


veh = Vehicle() # Vehicle.__init__(veh)   
veh.getCarDetail() # Vehicle.getCarDetail(veh)     