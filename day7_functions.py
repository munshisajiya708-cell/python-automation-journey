# functions programs

def hello():
    print("hello world")

hello()

def greet(name):
    print("Hello",name)
    
greet("sajiya")

print("Add numbers with function")
def add(a,b):
    print(a+b)

add(5,9)

print("Even or Odd")

def check(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

check(4)
        

print("Max of Two")

def maximum(a,b):
    return max(a,b)

print(maximum(5,9))

print("check prime")
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
         return False
    return True
print(is_prime(8))


print("Reverse string")
def reverse(s):
    return s[::-1]
print(reverse("python"))

print("count vowels")
def count(s):
    count=0
    for i in s:
        if i in "aeoiuAEIOU":
            count+=1
    return count
print(count("English grammer"))      

print("Login system using function")
def login(username,password):
    if username=="sajiya" and password=="12345":
     return "Login Succcess"
    else:
     return "Login Failed"
print(login("sajiya","12345"))


print("bill calculator")
def total_bill(price):
    return sum(price)
print(total_bill([100,2000,3000]))


     