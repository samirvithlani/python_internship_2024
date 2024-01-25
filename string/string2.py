name = "Ahmedabad"
#name = name + " is a good city"
name = name.upper()
print(name)
name = name.lower()
print(name)

# x = "B"
# print(ord(x))
# y = 97
# print(chr(y))


name1 = input("Enter name1: ")

for i in name1:
    if ord(i)>=97 and ord(i)<=122:
        print(chr(ord(i)-32),end="")
    




