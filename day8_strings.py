# string programs
name="sajiya"
print(name[0])
print(name[1])


print("string slicing")
name="sajiya"
print(name[0:3])

print("string functions")
text="python"
print(text.upper())
print(text.lower())
print(len(text))

print("checkin string")

text="python"
print("py"in text)


print("length of string")
s=input("enter string:")
print(len(s))

print("uppercase")
s=input("Eneter string:")
print(s.upper())

print("lowercase")
s=input("enetr string:")
print(s.lower())

print("Reverse string")
s=input("enter string:")
print(s[::-1])


print("count vowels")
s=input("enetr string:")
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print(count)



print("***Email validation***")

email=input("Enter email id:")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
    
    
print("login system")
username= input("enter username:")
password=input("enter pqassword:")

if username=="admin" and password=="12345":
    print("Login successful ")
else:
    print("Invalid username or password")
    

print("strength of password")
p = input("enter password::")
if len(p)>=8 :
    print("Strong password")
else:
    print("Weak password")
        