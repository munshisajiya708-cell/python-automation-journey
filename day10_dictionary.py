#dictionary programs

student={
    "name":"sajiya",
    "age":20,
    "course":"MCA"
}

print(student)
#Access data
print("Access data")

student={"name":"Ali",
         "age":23}
print(student["name"])

student={}
student["name"]="sajiya"
student["age"]=40
print(student)

#delete data
del student["age"]
print(student)

#update value
student={"name":"sajiya"}

student["name"]="Ali"
print(student)


#Student record system
print("Student record system")
student={}
student["name"]=input("Enter name:")
student["class"]=int(input("Enter class:"))
student["roll"]=int(input("Enter roll number:"))
print(student)

#login system
print("Login system")
user = {
    "username": "admin",
    "password": "1234"
}

u = input("Enter username: ")
p = input("Enter password: ")

if u == user["username"] and p == user["password"]:
    print("Login Success")
else:
    print("Wrong credentials")
    
#products price system
print("Products price system")
products = {
    "apple": 50,
    "banana": 20
}

item = input("Enter item: ")

print("Price:", products.get(item, "Not found"))
    