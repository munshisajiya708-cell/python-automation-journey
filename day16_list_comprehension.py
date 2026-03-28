# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, optionally filtering items using a condition.   
print("square list")
l=[1,2,3,4]
print([x*x for x in l])

print("Even numbers")
nums=[1,2,3,4]
even=([x for x in nums if x%2==0])
print(even)


print("Odd number")
nums=[1,2,3,4,5]
odd=([x for x in nums if x%2 !=0])
print(odd)


print("multiply by 10")
nums=[1,2,3]
print([x*10 for x in [1,2,3]])

print("uppercase")
l=["a","b"]
print([x.upper() for x in l])

print("length of string")
l=["hi","hello"]
print([len(x) for x in l])

print("filter")
l=[2,4,8]
print([x for x in l if x>5])

# real projecrt
print("real project")
salary=[10000,20000,30000]
bonus=([x+5000 for x in salary])
print(bonus)

print("student passed list")
marks = [30,50,80,20]

passed = [x for x in marks if x>=40]

print(passed)

print("clean data")

data = [1,2,0,3,0]

clean = [x for x in data if x!=0]

print(clean)

