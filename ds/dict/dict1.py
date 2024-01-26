# data  = {} # empty dictionary
# print(data)
# print(type(data))

data = {1:"Ahmedbad",2:"Surat",3:"Rajkot",2:"Bhavnagar"}
print(data)

data[4]="Vadodara"
data[3]="RAJKOT"
data.update({5:"Gandhinagar",6:"Junagadh"})
print(data)

removedValue = data.pop(2)
print("removing...",removedValue)
print(data)

x  = data.popitem()
print("removing...",x)
print(data)






