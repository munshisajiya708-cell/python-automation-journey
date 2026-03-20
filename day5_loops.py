#loops programs

#for loop
for i in range(1,11):
    print(i)
    
    for i in range(11):
        print(i)
# Even Numbers
print("...Even Numbers...")
for i in range(1,11):
    if i % 2==0:
        print(i)   
# Odd Numbers
print("....Odd Numbers.....")
for i in range(1,11):
    if i % 2 !=0:
        print(i)    
# Sum of numbers
print("****Sum of numbers****")
sum=0
for i in range(1,6):
    sum +=1
    print("Sum:",sum)     
     
#Multiplication Table
print("***Multiplication Table ****")

num = int(input("Enter Number:  "))
for i in range(1,11):
    print(num, "X" , i, "=", num*i)
#Reverse counting
print("reverse counting")
for i in range(30,0,-1):
    print(i)                   
#factorial
print("factorial")
num = int(input("Enter number: "))
fact=1
for i in range(1,num+1):
    fact*=i
    print("factorial:",fact)    
#While loop
print("while loop")
i=1
while i<=5:
    print(i)
    i+=1
#sum using while loop
print("sum using while loop")
i=1
sum=0
while i<=5:
    sum+=i
    i+=1
    print(sum)
# print table using while
print("table using while loop")
num=int(input("Enetr number:  "))
i=1
while i<=10:
    print(num*i)
    i+=1     
#break example
print("break example")
for i in range(10):
    if i ==5:
        break
    print(i)
# continue Example
print("continue example")
for i in range(10):
    if i == 5:
        continue
    print(i)             
#print square
print("print square")
for i in range(1,6):
    print(i*i)
# User Login attempts
print("*******User Login Attempts*******")
for i in range(3):
    password=input("Enter Password:  ")
    if password=="1234":
        print("Login Success")
    else:
        print("Try again")
#Bill Calculator
print("***Bill Calculator****")
total=0
for i in range(3):
    price=int(input("Enter Item Price:"))
    total+=price
    print("Total Bill:",total)
#Student Marks Average
print("***Student Marks Average*****")
total=0
for i in range(5):
    marks=int(input("Enter Marks:"))
    total+=marks
    avg=total/5
    print("Total Marks:",total)
    print("Average:",avg)                
        