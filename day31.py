#Day 31: OOP concepts with projects

class A:
   x= 10 
obj = A()
print(obj.x)

class Person:
    name="ALI"
p1=Person()
print(p1.name)

class Car:
    brand = "BMW"
c1 = Car()
print(c1.brand)

#student information

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Ali",45)
print("Name:",s1.name)
print("Age:",s1.age)

#car details:
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
c1=Car("BMW" ,"X4")
print("Brand:",c1.brand)
print("Model:",c1.model)


#bank
class Bank:
    def __init__(self,balance):
        self.balance = balance
    def deposite(self,amount):
         self.balance += amount
    
         print("New Balance:", self.balance)
b= Bank(1000)
b.deposite(500)


class Calculator:
    def add(self,a,b):
        print("Sum:", a+b)
        
c = Calculator()
c.add(10,5)

        
    
        
            