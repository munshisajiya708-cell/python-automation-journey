#day15_lambda_map_filter
print(" add lambda function")
add= lambda a,b:a+b
print(add(2,3))

print("square lambda function")
square=lambda x:x*x
print(square(5))

print("cube lambda function")
cube=lambda x:x*x*x
print(cube(3))

print("Even check")
even=lambda x :x%2==0
print(even(6))

print("odd check")
odd=lambda x:x%2 !=0
print(odd(5))

print("max of two numbers")
mx = lambda a,b: a if a>b else b
print(mx(5,9))

print("map function")
nums=[1,2,3]
print(list(map(lambda x:x*2,nums)))

#real projects
print("Salary increment")
salary=[10000,20000,30000]
new=list(map(lambda x:x+2000,salary))
print(new)

print("student passed filter")
marks=[30,50,80,20]
passed=list(filter(lambda x:x>=40,marks))
print(passed)

print("price discount")
price=[100,200,300]
discount=list(map(lambda x:x*0.9,price))
print(discount)

print("data clear")
data=[1,2,0,3,0]
clean=list(map(lambda x:x!=0,data))
print(clean)

