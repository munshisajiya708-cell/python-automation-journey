#calculator module
print("This is a calculator module")
import calc
print(calc.add(11,20))
print(calc.sub(22,3))


#file checker
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
    
#date time logger
import datetime
with open("log.txt","a") as f:
     f.write(str(datetime.datetime.now()) + "\n")
        
