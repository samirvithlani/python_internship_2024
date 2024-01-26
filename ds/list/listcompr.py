
# x = []
# for i in range(11):
#     x.append(i)
    
x = [i for i in range(11)]
print(x)

data = [100,20,30,40,50,60]

data1 = [i*10 for i in data]
print(data1)


data2 = [i for i in data if i>40]
print(data2)


users = ["ram","shyam","ghanshyam","radha","sita","gita","hari","radha"]

users1 = [i.upper() for i in users if len(i)>4]
print(users1)

users1 = [i for i in users if i.startswith("r") and len(i)>4]
print(users1)




