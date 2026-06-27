#Hashtable creation 
Student = { 
  "name":"Nikhil", 
  "age":20, 
  "cgpa":7.4
}
print(Student)

#insertion key-value pair 
Student["height"] = 6 
print(Student)

#deletion 
Student.pop("height")
print(Student)

#accessing a value 
print(Student["name"])
print(Student.get("name","Name not exist")) # if name not found then it'll return name not found . 

#updation 
Student["age"] = 22 
print(Student)

#Iterate through keys 
for key in Student : 
  print(key)

#Iterate through values 
for value in Student.values(): 
  print(value)

#Iterate key,value pair 
for key,value in Student.items(): 
  print("Key: ",key + " ,Value: ",value)



#Program for frequency counter 

arr = [1,2,2,1,3,2,1,3]
freq = {}
for num in arr : 
  freq[num] = freq.get(num,0)+1

print(freq)