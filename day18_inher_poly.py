#day 18 inheritence and polymorphism
class parent:
 def show(self):
  print("hello")
class child(parent):
 def hi(self):
  print("hi")
b=child()
b.show()
b.hi()
print("person student")
class person:
  def __init__(self,name):
   self.name=name
   
class student(person):
  def show(self):
      print(self.name)
s=student("johan")
s.show()
print("maths")
class A:
    def add(self,a,b):
        return a+b

class B(A):
    def mul(self,a,b):
        return a*b

b = B()
print(b.add(2,3))
print(b.mul(2,3))
print("student result")
class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def result(self,marks):
        if marks>=40:
            print("Pass")
        else:
            print("Fail")

s = Student("Sajiya")
s.result(50)
                 

              