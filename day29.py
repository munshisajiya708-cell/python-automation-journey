import requests

url = "https://api.github.com"

response = requests.get(url)

print(response.status_code)
print(response.text)



import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=your_api_key"

data = requests.get(url).json()

print(data)



import requests

data = requests.get("https://jsonplaceholder.typicode.com/users").json()

for user in data:
    print(user["name"])