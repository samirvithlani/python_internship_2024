subjects = ["C", "C++", "Java", "Python", "Android","Python"]


#ind = subjects.index("Python")
ind = subjects.index("Python",4,6)
print(ind)

# cnt  = subjects.count("Python1")
# print(cnt)
 
 
if subjects.count("ok")>0:
    print("ok is present")
    subjects.remove("ok")
else:
    print("ok is not present")    
    
    
# subjects.reverse() 
# print(subjects)   

#subjects.sort(reverse=True)
subjects.sort(key=len)
print(subjects)