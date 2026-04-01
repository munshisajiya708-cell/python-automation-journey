import requests
url = "https://httpbin.org/post"
data={
    "name":"sajiya",
    "course":"python"
}
response=requests.post(url,data=data)
print(response.status_code)
print(response.text)
print(response.json())
