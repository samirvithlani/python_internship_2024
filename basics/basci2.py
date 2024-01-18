#scanf, input function..
#input function by default returns string

# no1 = input("Enter a number: ")
# print("You entered: ", no1+100) #"100"

# print(type(no1)) #<class 'str'>
# int no1 = 100.20 --> no1 -> 100

no1 = int(input("Enter a number: "))
print("You entered: ", no1+100) #100
print(type(no1)) #<class 'int'>


per = float(input("Enter percentage: "))
print("You entered: ", per) 
print(type(per)) #<class 'float'>


isPadssed = bool(input("Enter True/False: "))
print("You entered: ", isPadssed)
print(type(isPadssed)) #<class 'bool'>