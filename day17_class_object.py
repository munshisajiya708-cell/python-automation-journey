#day 17 class and object

class student:
 def __init__(self, name):
  self.name= name
    
s1=student("Ali")
s2=student("Sajiya")
s3=student("sara")
        
print(s1.name)
print(s2.name)
print(s3.name)

class student1:
 def __init__(self,name,age):
  self.name=name
  self.age=age
    
s1=student1("Ali",20)
s2=student1("sajiya",32)
print(s1.name)
print(s1.age)

class student2:
 def __init__(self,subject,marks):
  self.subject=subject
  self.marks=marks
s1=student2("math",89)
print(s1.subject)
print(s1.marks)

#banking
class Bank:
 def __init__(self,balance):
  self.balance=balance
 def deposite(self,amt):
  self.balance+=amt
 def show(self):
  print(self.balance)
b1=Bank(1000)
b1.deposite(500)
b1.show()


print("addtion method")
class calc:
  def add(self,a,b):
   print(a+b)
         
c1=calc()
c1.add(5,9)

print("subtraction method")
class calc:
  def sub(self,a,b):
    print(a-b)
c1=calc()
c1.sub(9,5)

print("square method")
class square:
 def square(self,x):
     print(x*x)
s1=square()
s1.square(6)

print("cube method")
class cube:
  def cube(self,x):       
   print(x*x*x)
c1=cube()
c1.cube(3)

print("Even or oddd method")
class check:
   def even(slef,x):
     if x%2==0:
      print("Even")
     else:
      print("odd")
c1=check()
c1.even(6)

print("print details")
class employee:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def show(self):
   print(self.name,self.age)
e1=employee("Ali",25)
e1.show()
       
print("student management system")
class Student:
  def __init__(self,name,marks):
   self.name = name
   self.marks = marks

  def result(self):
    if self.marks >= 40:
     print("Pass")
    else:
     print("Fail")

s = Student("Sajiya",50)
s.result()
print("Login system")
class user:
  def login(self,username,password):
    if username=="admin" and password=="1234":
     print("Login successful")
    else:
     print("Login failed")
u1=user()
u1.login("admin","1234")
                                  
           
      

    
        