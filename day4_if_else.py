#if condition
num= 10
if num>5:
    print("Number is greater")
else:
    print("Number is smaller")

#Even or Odd
num=int(input("Enter number:  "))
if num%2==0 :
    print("Even")
else:
    print("Odd")
    
#Positive and Negative number
num=int(input("Enter number: "))
if num>0:
    print("Positive")
else:
    print("Negative")
    
#Number greater or smaller
num=int(input("Enter number:"))
if num>10:
    print("Greater than 10")
else:
    print("smaller than 10" )

#checking vote eleigibility
age = int(input("Enter age:  "))
if age>=18:
    print("You can vote")
else:
    print("You can not vote")
    
#Pass and Fail 
marks = int(input("Enter Marks:"))
if marks>=40:
 print("Pass")
else:
    print("Fail")
    
#Largest two number
a=int(input("Enetr first number:"))
b=int(input("Enetr Second number:"))
if a>b:
    print("A is greater")
else:
    print("B is greater")


#check divisible by 5

num=int(input("Enter number"))
if num%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

#check username
name=input("Enter username: ")
if name=="admin":
    print("Welcome admin")
else:
    print("Access Denied")
#Temperature check
temp=int(input("Enter temperature:"))
if temp>30:
    print("Hot")
else:
    print("Normal")
    
####Login system
username=input("Enter username:  ")
password=input("Enter Password: ")
if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Invalid credentials")

#Discount system
amount=int(input("enter amount:"))
if amount>1000:
    print("Discount applied") 
else:
    print("No Discount")

#Grade system
marks= int(input("Enter marks:"))
if marks>=90:
    print("Grade A+")
else:
    print("Grade A")                           
     