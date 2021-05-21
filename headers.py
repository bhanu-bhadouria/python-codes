import requests
url="https://icanhazdadjoke.com/"
response=requests.get(url,headers={"accept":"application/json"})
data = response.json()
print(data["joke"])
