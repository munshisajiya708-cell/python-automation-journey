import requests
url = "https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
print(response.status_code)
data=response.json()
print(data[0])
for post in data:
    print(post["username"], "-", post["id"], "-" , post["phone"], "-")
 
 
print("weather api")
 
import requests

city = input("Enter city: ")

url = f"https://wttr.in/{city}?format=j1"

data = requests.get(url).json()

print(data["current_condition"][0]["temp_C"])   

import requests,json

data=requests.get("https://jsonplaceholder.typicode.com/posts").json()

with open("posts.json","w") as f:
    json.dump(data,f)
    
    
    

