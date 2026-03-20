#list programs
numbers=[1,2,3,4,5]
print(numbers)

#index example
fruits=["apple","banana","mango"]
print(fruits[0])
print(fruits[2])

#Add elements of list
fruits=["apple","banana","mango"]
fruits.append("Pineapple")
print(fruits)

#Remove elements of list
fruits=["apple","banana","mango"]
fruits.remove("banana")
print(fruits)

#length of list
numbers=[1,2,3,4,5]
print(len(numbers))

#loop python list
numbers=[1,2,3]
for num in numbers:
    print(num)

#sum of list
numbers=[1,2,3,4]
total = 0
for num in numbers:
    total += num
    print("Sum:",total)
    
#Largest number in list
numbers = [5, 10, 3, 8]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)

#count in list
numbers=[1,2,3,4,5]
count=0
for num in numbers:
    count+=1
    print("Count:",count)

#Even numbers in list
print("**Even Numbers**")

numbers=[1,2,3,4,5]
for num in numbers:
    if num%2==0:
     print("Even numbers:",num)


#Reverse number in list
("**Reverse number:**")
numbers=[1,2,3,4,]
numbers.reverse()
print(numbers)

#user input list
numbers=[]
for i in range(3):
    num=int(input("Enter numbers:"))
    numbers.append(num)
    print("Numbers:",numbers)

#Shopping list
print("**Shopping List**")
items=[]
for i in range(5):
    item=input("Enter items: ")
    items.append(item)
    print("Shopping List:",items)
 
#Student Marks list
print("**Student Marks**")
marks=[]
for i in range(5):
    m=int(input("Enter Marks:  "))
    marks.append(m)
    total=sum(marks)
    avg=total/5
    print("Total Marks:",total)
    print("Average marks:",avg)


#Remove items in system
print("*Removes item*")
items=["pen","book","pencil","eraser"]
remove_item=input("Enter item to remove:")
if remove_item in items:
    items.remove(remove_item)
    print("Updated list:",items)
else:
    print("Item not found in list")
            
    