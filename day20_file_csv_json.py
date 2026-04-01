f = open("data1.txt","w")
f.write("Hello world")
f.close()

f=open("data1.txt","r")
print(f.read())
f.close()

f=open("data1.txt","a")
f.write("\nwelcome to python")
f.close()
with open("data1.txt","r") as f:
    print(f.read())

import csv
with open("data1.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["name", "age",  "city"])
    writer.writerow(["Sara",  25,     "Pune"])
    writer.writerow(["Ali",   24,     "Mumbai"])

import csv
with open("data1.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
        
import json
data={"name": "sajiya","age": 25,"city": "Pune"}
with open("data1.json","w")as f:
    json.dump(data,f)
with open("data1.json","r") as f:
    data=json.load(f)
    
print(data)

print("student csv system")
import csv

with open("students.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Subjects","Marks"])
    w.writerow(["Maths",80])
with open("students.csv","r")as f:
    r=csv.reader(f)
    for row in r:
        print(row)
        
print("backup system")
with open("data1.txt") as f:
    data=f.read()

with open("backup.txt","w") as f:
    f.write(data)        
        