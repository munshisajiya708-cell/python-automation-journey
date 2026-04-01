class A:
    x = 10

a = A()
print(a.x)

class A:
    def __init__(self):
        self._x = 20

a = A()
print(a._x)

class Test:
    def __init__(self):
        self.__num = 100

    def get(self):
        return self.__num

t = Test()
print(t.get())


class Test:
    def __init__(self):
        self.__num = 0

    def set(self,n):
        self.__num = n

    def get(self):
        return self.__num

t = Test()
t.set(50)
print(t.get())


class Bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amt):
        self.__balance += amt

    def show(self):
        print(self.__balance)

b = Bank()
b.deposit(500)
b.show()

class User:
    def __init__(self):
        self.__password = "123"

    def login(self,p):
        if p == self.__password:
            print("Success")

u = User()
u.login("123")


from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Square")

s = Square()
s.area()

print("real project")

class Bank:
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amt):
        self.__balance += amt

    def withdraw(self,amt):
        if amt<=self.__balance:
            self.__balance -= amt

    def show(self):
        print(self.__balance)

b = Bank()
b.deposit(500)
b.withdraw(200)
b.show()

class User:
    def __init__(self):
        self.__password = "admin"

    def login(self,p):
        if p == self.__password:
            print("Login success")
        else:
            print("Wrong")

u = User()
u.login("admin")


class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee(50000)
print(e.get_salary())
