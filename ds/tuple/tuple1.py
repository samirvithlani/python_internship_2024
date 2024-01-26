data = (10,20,40,50,78)

print(data)
print(type(data))

x = data.count(10)
print(x)

ind = data.index(50)
print(ind)


#data[0]= 1000

a = (10,20,30)
b = (40,50,60)

x = a+b
print(x)



dataList = list(data)
dataList[0] = 100

data = tuple(dataList)
print(data)


