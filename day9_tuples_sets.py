#tuples
t=(1,2,3)
print(t)

#Acccess tuples
t=(10,20,30)
print(t[0])

#length tuples
print("length of tuples")
t=(1,2,3,4)
print(len(t))

#loop tuples
print("Loop tuples")
t=(1,2,3)
for i in t:
 print(i)

#Count elements
print("count elements")
t=(1,2,2,3,4,2)
print(t.count(2))
 
#indexs find
print("index find")
t=(15,10,5)
print(t.index(5))

#Tuple list
print("tiple list")
t=(1,2,3)
l=list(t)
print(l)

#max and min
print("max and min")
t=(19,21,8)
print(max(t))
print(min(t))
 
#part -2 sets
print("sets")
s={1,2,2,3}
print(s)

#add in set
print("Add element in set") 
s={1,2,3}
s.add(4)
print(s)

 #Remove in set
print("Remove element in set") 
s={1,2,3,4}
s.remove(4)
print(s)

#lopp set
print("loop set")
s={1,2,3}
for i in s:
 print(i)
 
#length of set
print("length of set")
s={1,2,3,4}
print(len(s))

#unioin of set
print("union of set")
a={1,2}
b={2,3}
print(a|b)

#intersection of set
print("intersection of set")
a={1,2}
b={2,3}
print(a&b)

#difference of set
print("difference of set")
a={1,2}
b={2,3}
print(a-b)

 #check element
print("check element in set")
s = {1,2,3}
print(2 in s)

#Remove Duplicate names
print("Remove Duplicate names")
names = ["Ali","Sajiya","Ali"]
unique = set(names)
print(unique)

nam=["sara", "farhat", "sara"]
unique = set(nam)
print(unique)

#Students marks
print("Students marks")
marks=(50,50,50)
print("average marks:",sum(marks)/len(marks))

#common friends finder
print("common friends finder")
a={"Ali","sajiya","sam"}
b={"sajiya","sam","farhat"}
print("common friends:",a&b
      )