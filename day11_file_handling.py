#file handling
file=open("data.txt","w")
file.write("hello pythpn")
file.close()

 

 
 #count characters
print("Count characters")
with open("file.txt","r") as f:
  data= f.read()
  print(len(data))
  
file.close()
 #copy file
 
with open("file.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)
    
 #remove empty lines
with open("file.txt","r") as f:
    lines=f.readlines()
with open("clean.txt","w") as f:
      for line in lines:
          if line.strip() !="":
              f.write(line)     
 
 
 #uppercase file
with open("file.txt", "r") as f:
    data = f.read().upper()

with open("upper.txt", "w") as f:
    f.write(data)  
    
#lower case file
with open("file.txt","r") as f:
    data=f.read().lower()
    
with open("lower.txt","w") as f:
    f.write(data)
    
#daily report generator    
name = input("Enter name: ")
task = input("Enter task: ")

with open("report.txt", "a") as f:
    f.write(f"{name} completed {task}\n")    
    
#notes saver
print("notes saver")

notes=input("Write notes:")
with open("notes.txt","a") as f :
    f.write(notes + "\n")


#file backup strip
with open("notes.txt","r") as f:
    data= f.read()
    
with open("backup.txt", "w") as f:
    f.write(data)        

with open("notes.txt", "r") as f:
    data = f.read()

with open("backup.txt", "w") as f:
    f.write(data)             
           
 
